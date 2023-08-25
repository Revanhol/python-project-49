from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    count = 0
    if number < 2:
        return False
    for i in range(2, int(number // 2 + 1)):
        if number % i == 0:
            count += 1
            return False
    if count == 0:
        return True


def generate_question_and_right_answer():
    number = randint(1, 100)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return f"{number}", answer
