import prompt

count_of_tries = 3


def start_game(game_name):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game_name.game_rules)
    try_count = 1
    while try_count <= count_of_tries:
        number, answer = game_name.create_question()
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == answer:
            print('Correct!')
            try_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
