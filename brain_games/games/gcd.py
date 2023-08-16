from random import randint
from math import gcd

game_rules = 'Find the greatest common divisor of given numbers.'


def create_question():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operation = gcd(number_1, number_2)
    answer = str(operation)
    number = f"{number_1} {number_2}"
    return number, answer