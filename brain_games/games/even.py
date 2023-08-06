from random import randint

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_question():
    number = randint(1, 100)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    number = str(number)
    return number, answer
