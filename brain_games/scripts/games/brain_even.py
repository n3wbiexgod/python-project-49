from random import randint
from brain_games.cli import welcome_user


def get_user_answer(number):
    print(f'Question: {number}')
    return input('Your answer: ')


def is_answer_correct(number, user_answer):
    return 'yes' if number % 2 == 0 else 'no' == user_answer


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0
    while correct_answers_count < 3:
        number = randint(1, 100)
        user_answer = get_user_answer(number)
        if is_answer_correct(number, user_answer):
            print('Correct!')
            correct_answers_count += 1
        else:
            correct_answer = 'yes' if number % 2 == 0 else 'no'
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
