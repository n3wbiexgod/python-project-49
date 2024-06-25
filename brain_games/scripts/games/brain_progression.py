import random
from brain_games.scripts.games.game_engine import run_game


GAME_NAME = 'Brain Progression'
DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]


def generate_question():
    progression_length = random.randint(5, 10)
    progression_start = random.randint(1, 10)
    progression_step = random.randint(1, 10)
    progression = generate_progression(progression_start, progression_step, progression_length)
    hidden_element_index = random.randint(0, progression_length - 1)
    progression[hidden_element_index] = '..'
    question = ' '.join(map(str, progression))
    return question, progression_start, progression_step, hidden_element_index


def correct_answer_function(question_data):
    _, start, step, hidden_element_index = question_data
    return start + step * hidden_element_index


def main():
    run_game(GAME_NAME, DESCRIPTION, generate_question, correct_answer_function)

if __name__ == '__main__':
    main()
