from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i <= sqrt(number):
        if number % i == 0:
            return False
        i += 2
    return True
