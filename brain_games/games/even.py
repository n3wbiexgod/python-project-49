from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    """Создает вопрос и определяет, является ли число четным."""
    task = randint(1, 100)
    flag = is_even(task)
    if flag is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, task


def is_even(task):
    return True if task % 2 == 0 else False
