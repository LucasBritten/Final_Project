# Lucas Britten
# CMPSC 132 Final Project --> Number Guessing Game
# Includes Optional Enhacements

import random

def get_random_number(difficulty):
    """Return a random number based on difficulty level."""
    if difficulty == "easy":
        return random.randint(1, 50)
    elif difficulty == "medium":
        return random.randint(1, 100)
    elif difficulty == "hard":
        return random.randint(1, 200)
    else:
        return random.randint(1, 100)

def get_guess():
    """Prompt user for a valid integer guess."""
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """Main game loop."""
    print("\nWelcome to the Number Guessing Game!")
    print("Choose a difficulty level: easy / medium / hard")
    difficulty = input("Difficulty: ").strip().lower()
    if difficulty == "easy":
        print("Guess a number between 1 and 50.")
    elif difficulty == "medium":
        print("Guess a number between 1 and 100.")
    elif difficulty == "hard":
        print("Guess a number between 1 and 200.")
    else:
        print("Guess a number between 1 and 100.")


    number = get_random_number(difficulty)
    attempts = 0

    # Set attempt limits by difficulty
    limits = {"easy": 10, "medium": 7, "hard": 5}
    max_attempts = limits.get(difficulty, 7)

    print(f"You have {max_attempts} attempts to guess the number! Good luck!")

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        if guess < number:
            print("Too low! Try a higher number.")
        elif guess > number:
            print("Too high! Try a lower number.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"Out of attempts! The correct number was {number}.")

    print("\nWould you like to play again? (yes/no)")
    replay = input("> ").strip().lower()
    if replay == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
