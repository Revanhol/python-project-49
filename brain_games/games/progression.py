import random

game_rules = 'What number is missing in the progression?'


def create_question():
    first_number = random.randint(1, 10)
    last_number = random.randint(11, 100)
    step_number = random.randint(1, 5)
    progression = list(range(first_number, last_number, step_number))
    change_index = random.randint(0, len(progression) - 1)
    answer = str(progression[change_index])
    progression[change_index] = '..'
    number = ' '.join(map(str, progression))
    return number, answer