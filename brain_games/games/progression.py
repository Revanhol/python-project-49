import random

GAME_RULES = 'What number is missing in the progression?'


def creating_a_question_and_a_correct():
    first_number = random.randint(1, 10)
    last_number = random.randint(30, 180)
    step_number = random.randint(2, 5)
    progression = list(range(first_number, last_number, step_number))
    change_index = random.randint(0, len(progression) - 1)
    answer = str(progression[change_index])
    progression[change_index] = '..'
    number = ' '.join(map(str, progression))
    return number, answer
