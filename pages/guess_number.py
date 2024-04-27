from art import guess_number_logo
import os
import random as r

# Set the TERM environment variable to 'xterm' (a common terminal type)
os.environ['TERM'] = 'xterm'


# Now you can use the clear function as before
def clear_console():
    """Clears the console screen."""
    os.system('clear')


# check for difficulty level
def difficulty_assignment():
    """Check for difficulty and return number (integer) of attempts based on response.
    10 for easy, 5 for hard, 0 for invalid response."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty.lower() == "hard":
        print("You have 5 attempts to guess the number.")
        return 5
    elif difficulty.lower() == "easy":
        print("You have 10 attempts to guess the number.")
        return 10
    else:
        print("That was an invalid response.")
        return 0


# evaluate the guess
def check_guesses(user_guess, correct_number):
    if user_guess > correct_number:
        print("Too high.")
    elif user_guess < correct_number:
        print("Too low.")
    elif user_guess == correct_number:
        return True


def exit_gracefully(result, correct_number):
    # Call the function to clear the console
    clear_console()
    print(guess_number_logo)
    if result == 0:
        return f"Sorry, but you've run out of guesses.\nThe winning number was {correct_number}.\nThanks for playing!"
    else:
        return f"You got it! The answer was {correct_number}.\nGreat job!!"


def game():
    # beginning housekeeping
    clear_console()
    print(guess_number_logo)

    # establish winning number
    winning_number = r.randint(1, 100)

    # intro and welcome
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    # print(f"Pssst, the correct answer is {str(winning_number)}")

    # determine number of guesses based on difficulty level chosen in function, above
    max_guesses = difficulty_assignment()

    # handle for invalid response to difficulty level check
    if max_guesses == 0:
        print("Please try again.")
        max_guesses = difficulty_assignment()
        if max_guesses == 0:
            print("Sorry, but you were given two opportunities to provide a valid response, \
            and did not do so either time.\nHave a nice day!")

    # loop to take guesses
    while max_guesses > 0:
        guess = int(input("Make a guess: "))
        you_win = check_guesses(guess, winning_number)
        if you_win:
            max_guesses = -1
            break
        else:
            max_guesses -= 1
        if max_guesses > 0:
            print("Guess again.")
            if max_guesses > 1:
                print(f"You have {max_guesses} attempts remaining to guess the number.")
            else:
                print("You have 1 attempt remaining to guess the number.")

    # exit gracefully
    ending = exit_gracefully(max_guesses, winning_number)
    print(ending)
    print()
    print()


if __name__ == "__guess_number__":
    game()

# Number Guessing Game Objectives:
# Include an ASCII art logo.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# Allow the player to submit a guess for a number between 1 and 100.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
