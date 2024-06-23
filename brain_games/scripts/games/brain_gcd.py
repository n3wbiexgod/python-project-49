import random
from math import gcd
from brain_games.scripts.games.game_engine import run_game

DESCRIPTION = "Find the greatest common divisor of given numbers."

def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return f"{number1} {number2}"

def correct_answer(question):
    number1, number2 = map(int, question.split())
    return str(gcd(number1, number2))

def main():
    run_game('GCD Game', DESCRIPTION, generate_question, correct_answer)

if __name__ == '__main__':
    main()
