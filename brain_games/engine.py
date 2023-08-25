import prompt

COUNT_OF_TRIES = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.GAME_RULES)
    for _ in range(COUNT_OF_TRIES):
        number, answer = game.generate_question_and_right_answer()
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let\'s try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
