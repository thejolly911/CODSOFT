import random

def generate_random_number(start, end):
    return random.randint(start, end)

def get_user_guess():
    return int(input("Enter your guess: "))

def compare_guesses(user_guess, random_number):
    if user_guess == random_number:
        return "Correct!"
    elif user_guess < random_number:
        return "Too low!"
    else:
        return "Too high!"

def play_game():
    random_number = generate_random_number(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        attempts += 1
        user_guess = get_user_guess()
        result = compare_guesses(user_guess, random_number)

        if result == "Correct!":
            print(f"You won! It took you {attempts} attempts.")
            return True

        print(result)

    if attempts == max_attempts:
        print("You lost! The number was not guessed within the attempt limit.")
        return False

def play_multiple_rounds():
    rounds = 3
    score = 0

    for _ in range(rounds):
        if play_game():
            score += 1

    print(f"Your final score is {score}/{rounds}.")

play_multiple_rounds()