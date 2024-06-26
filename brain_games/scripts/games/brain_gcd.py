import random
import prompt


def gcd(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nFind the greatest common divisor of given numbers.')
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        correct_answer = gcd(num1, num2)
        if int(answer) == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
