import operator
import random

game_rules = 'What is the result of the expression?'


def create_question():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    choice = random.randint(1, 3)
    if choice == 1:
        action = "+"
        operation = operator.add(number_1, number_2)
    elif choice == 2:
        action = "-"
        operation = operator.sub(number_1, number_2)
    else:
        action = "*"
        operation = operator.mul(number_1, number_2)
    answer = str(operation)
    number = f"{number_1} {action} {number_2}"
    return number, answer
