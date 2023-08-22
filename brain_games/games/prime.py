from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = 2
    count = 0
    while i < number // 2:
        if number % i == 0:
            count += 1
            return False
        else:
            i += 1
    if count == 0:
        return True


def creating_a_question_and_a_correct():
    number = randint(2, 100)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return str(number), answer
