from flask import Blueprint, render_template, redirect, url_for, abort, request
from flask_login import login_required, current_user
from task.forms import TodoForm
from models import Task
from run import db

task = Blueprint('task', __name__)


@task.route('/task', methods=['POST', 'GET'])
@login_required
def create_todo():
    form = TodoForm()
    user_tasks = Task.query.filter_by(
        user_id=current_user.id).order_by(Task.id.desc())
    if form.validate_on_submit():
        task = Task(task=form.user_task.data, done=False, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task.create_todo'))
    return render_template('todo.html', title="todo", form=form, user_tasks=user_tasks, model_title="new task to do")


@task.route('/task/<int:task_id>/delete', methods=['POST', 'GET'])
@login_required
def delete(task_id):
    user_task = Task.query.get_or_404(task_id)
    if user_task.author != current_user:
        abort(403)
    db.session.delete(user_task)
    db.session.commit()
    return redirect(url_for('task.create_todo'))


@task.route('/task/<int:task_id>/done-true', methods=['POST', 'GET'])
@login_required
def change_done_true(task_id):
    user_task = Task.query.get_or_404(task_id)
    user_task.done = True
    db.session.commit()
    return redirect(url_for('task.create_todo'))


@task.route('/task/<int:task_id>/done-false', methods=['POST', 'GET'])
@login_required
def change_done_false(task_id):
    user_task = Task.query.get_or_404(task_id)
    user_task.done = False
    db.session.commit()
    return redirect(url_for('task.create_todo'))


@task.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(task_id):
    user_task = Task.query.get_or_404(task_id)
    if user_task.author != current_user:
        abort(403)
    form = TodoForm()
    if form.validate_on_submit():
        user_task.task = form.user_task.data
        db.session.commit()
        return redirect(url_for('task.create_todo'))
    elif request.method == 'GET':
        form.user_task.data = user_task.task
    return render_template('edit.html', form=form, user_task=user_task)


@task.route('/task/delete_all_done', methods=['POST', 'GET'])
@login_required
def delete_all_done():
    user_task = Task.query.filter_by(user_id=current_user.id).filter(Task.done==1)
    for _i in user_task:
        db.session.delete(_i)
        db.session.commit()
    return redirect(url_for('task.create_todo'))
