import prompt
import random


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_user_answer(name):
    random_num = random.randint(2, 30)
    print(f'Question: {random_num}')
    answer = prompt.string('Your answer: ')
    result = 'yes' if is_prime(random_num) else 'no'
    return answer, result, random_num


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}! Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        answer, result, random_num = get_user_answer(name)
        if answer == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
