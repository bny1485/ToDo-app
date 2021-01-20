
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from task.forms import Todo
from models import Task
from run import db

task = Blueprint('task', __name__)


@task.route('/task', methods=['POST', 'GET'])
@login_required
def create_todo():
    form = Todo()
    user_tasks = Task.query.filter_by(
        user_id=current_user.id).order_by(Task.id.desc())
    if form.validate_on_submit():
        task = Task(task=form.user_task.data, done=False, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task.create_todo'))
    return render_template('todo.html', title="todo", form=form, user_tasks=user_tasks, model_title="new task to do")
