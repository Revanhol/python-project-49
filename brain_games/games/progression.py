import random

GAME_RULES = 'What number is missing in the progression?'


def generate_question_and_right_answer():
    first_number = random.randint(1, 10)
    last_number = random.randint(30, 180)
    step_number = random.randint(2, 5)
    progression = list(range(first_number, last_number, step_number))
    random_index = random.randint(0, len(progression) - 1)
    answer = f"{progression[random_index]}"
    progression[random_index] = '..'
    number = ' '.join(map(str, progression))
    return number, answer
