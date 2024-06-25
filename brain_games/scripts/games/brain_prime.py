import random
from brain_games.scripts.games.game_engine import run_game


DESCRIPTION = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_round():
    number = random.randint(1, 100)
    return number


def correct_answer_function(number):
    return 'yes' if is_prime(number) else 'no'


def main():
    run_game("Prime Game", DESCRIPTION, generate_round, correct_answer_function)

if __name__ == '__main__':
    main()
