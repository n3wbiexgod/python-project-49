import random
from brain_games.game_engine import run_game
from brain_games.scripts.games.brain_calc import main as play_game


DESCRIPTION = "What is the result of the expression?"


def generate_round():
    operations = ['+', '-', '*']
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"

    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 * number2)

    return question, correct_answer


def main():
    run_game(DESCRIPTION, generate_round)

if __name__ == '__main__':
    main()
