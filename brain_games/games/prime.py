from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    prime = True
    if number < 2:
        prime = False
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            prime = False
    return prime


def generate_question_and_right_answer():
    number = randint(1, 100)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return f"{number}", answer
