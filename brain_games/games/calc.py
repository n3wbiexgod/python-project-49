from operator import add, sub, mul

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul
}


def make_question():
    first_number, second_number = randint(1, 50), randint(1, 50)
    operator = choice(list(OPERATORS.keys()))
    correct_answer = str(OPERATORS[operator](first_number, second_number    task = f'{first_number} {operator} {second_number}'

    return correct_answer, task
