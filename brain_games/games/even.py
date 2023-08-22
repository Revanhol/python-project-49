from random import randint

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def creating_a_question_and_a_correct():
    number = randint(1, 100)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(number), answer
