import random
from brain_games.scripts.games.game_engine import run_game


DESCRIPTION = "What is the result of the expression?"


def generate_question():
    operations = ['+', '-', '*']
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"
    return question


def correct_answer_function(question):
    number1, operation, number2 = question.split()
    number1 = int(number1)
    number2 = int(number2)

    if operation == '+':
        return str(number1 + number2)
    elif operation == '-':
        return str(number1 - number2)
    elif operation == '*':
        return str(number1 * number2)


def main():
    game_name = "Brain Calc Game"
    game_description = DESCRIPTION
    run_game(game_name, game_description, generate_question, correct_answer_function)

if __name__ == '__main__':
    main()
