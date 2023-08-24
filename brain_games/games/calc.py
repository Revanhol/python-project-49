import random

GAME_RULES = 'What is the result of the expression?'


def generate_question_and_right_answer():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operator = random.choice('+-*')
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    number = f"{number_1} {operator} {number_2}"
    return number, f"{result}"
