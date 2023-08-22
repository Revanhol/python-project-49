from random import randint
from math import gcd

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def creating_a_question_and_a_correct():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operation = gcd(number_1, number_2)
    answer = str(operation)
    number = f"{number_1} {number_2}"
    return number, answer
