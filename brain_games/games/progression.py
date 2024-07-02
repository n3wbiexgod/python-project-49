from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def make_progression():
    """Генерирует арифметическую прогрессию и определяет пропущенное число."""
    task = []
    initial_number = randint(0, 50)
    difference = randint(1, 10)
    length = 10
    for _ in range(length):
        task.append(initial_number)
        initial_number += difference

    random_index = randint(0, length - 1)
    correct_answer = str(task[random_index])
    task[random_index] = '..'
    return task, correct_answer


def make_question():
    """Формирует вопрос с прогрессией, где одно из чисел заменено на '..'"""
    task, correct_answer = make_progression()
    task_display = ' '.join(str(i) for i in task)
    return correct_answer, task_display
