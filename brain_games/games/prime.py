from random import randint

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def create_question():
    number = randint(2, 100)
    count = 0
    i = 2
    while i < number // 2:
        if number % i == 0:
            count += 1
            i += 1
        else:
            i += 1
    if count == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(number), answer
