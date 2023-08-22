import random

GAME_RULES = 'What is the result of the expression?'


def creating_a_question_and_a_correct_answer():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operator = random.choice('+-*')
    if operator == "+":
        action = number_1 + number_2
    elif operator == "-":
        action = number_1 - number_2
    else:
        action = number_1 * number_2
    answer = str(action)
    number = f"{number_1} {operator} {number_2}"
    return number, answer
