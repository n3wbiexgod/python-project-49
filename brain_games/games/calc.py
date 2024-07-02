from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul
}


def make_question():
    """Генерирует математический вопрос и правильный ответ."""
    first_number, second_number = randint(1, 50), randint(1, 50)
    operator = choice(list(OPERATORS.keys()))
    correct_answer = str(OPERATORS[operator](first_number, second_number))
    task = f'Question: {first_number} {operator} {second_number}'
    return correct_answer, task
