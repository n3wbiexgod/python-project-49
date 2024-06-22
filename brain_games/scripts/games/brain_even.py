from random import randint
from brain_games.cli import welcome_user


def play_round():
    number = randint(1, 100)
    print(f'Question: {number}')
    user_answer = input('Your answer: ')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0
    while correct_answers_count < 3:
        if play_round():
            correct_answers_count += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if correct_answers_count == 3:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
