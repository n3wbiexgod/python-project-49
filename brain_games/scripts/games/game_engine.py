import random


def generate_number():
    return random.randint(1, 100)


def is_even(number):
    return number % 2 == 0


def calculate(expression):
    # Remember to be cautious with eval!
    return eval(expression)


def run_game(game_name, game_description, generate_question, correct_answer_function):
    print(game_name)
    print(game_description)
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        question = generate_question()
        correct_answer = correct_answer_function(question)
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is the wrong answer ;(. The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers_count == correct_answers_needed:
        print(f"Congratulations, {name}!")
