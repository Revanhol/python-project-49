import prompt

COUNT_OF_TRIES = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.GAME_RULES)
    for try_count in range(COUNT_OF_TRIES):
        number, answer = game.creating_a_question_and_a_correct()
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == answer:
            print('Correct!')
            try_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let\'s try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
