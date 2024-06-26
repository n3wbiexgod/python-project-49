import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    i = 0
    result = ''
    name = prompt.string('May I have your name? ')
    print(
        f'Hello, {name}!\nAnswer "yes" if the number is even, '
        'otherwise answer "no".'
    )
    while i < 3:
        num = random.randint(1, 100)
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer "
                f"was {result}.\nLet's try again, {name}!"
            )
            break
        i = i + 1
    if i == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
