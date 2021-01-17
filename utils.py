
from random import randint

def secret_key_generator():
    w = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789'
    random_string = ''
    for _i in range(50):
        chose = randint(0, len(w)-1)
        random_string += w[chose]
    return random_string


random_string = secret_key_generator()