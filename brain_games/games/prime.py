from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Проверяет, является ли число простым."""
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i <= sqrt(number):
        if number % i == 0:
            return False
        i += 2
    return True


def make_question():
    """Генерирует случайное число и задает вопрос, является ли оно простым."""
    number = randint(1, 100)
    question = f'Question: {number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return correct_answer, question
