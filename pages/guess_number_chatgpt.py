import streamlit as st
from art import guess_number_logo
import random

# Function to clear the console
def clear_console():
    st.write("\n" * 100)

# Function to check for difficulty level and return number of attempts
def difficulty_assignment():
    if "difficulty" not in st.session_state:
        st.session_state.difficulty = "not_set"
    difficulty = st.selectbox("Choose a difficulty:", ["Not set", "Easy", "Hard"])
    if difficulty.lower() == "hard":
        st.write("You have 5 attempts to guess the number.")
        return 5
    elif difficulty.lower() == "easy":
        st.write("You have 10 attempts to guess the number.")
        return 10
    else:
        st.write("Please choose a difficulty.")
        return 0

# Function to evaluate the guess
def check_guesses(user_guess, correct_number):
    if user_guess > correct_number:
        st.write("Too high.")
    elif user_guess < correct_number:
        st.write("Too low.")
    else:
        return True

# Main game function
def game():
    st.title("Number Guessing Game")
    st.markdown(guess_number_logo)

    # Initialize winning number and attempts if not already set
    if "winning_number" not in st.session_state:
        st.session_state.winning_number = 0

    if "max_guesses" not in st.session_state:
        st.session_state.max_guesses = 0

    st.session_state.max_guesses -= 1
    
    # Generate a random number if not already generated
    if st.session_state.winning_number == 0:
        st.session_state.winning_number = random.randint(1, 100)

    st.write('Pssst, the correct answer is ', st.session_state.winning_number)

    # Determine number of guesses based on difficulty level
    max_guesses = difficulty_assignment()

    # Handle for invalid response to difficulty level check
    if max_guesses == 0:
        st.write("Please try again.")
        max_guesses = difficulty_assignment()
        if max_guesses == 0:
            st.write("Sorry, but you were given two opportunities to provide a valid response, "
                     "and did not do so either time.\nHave a nice day!")

    # Loop to take guesses
    while max_guesses > 0:
        with st.empty():
            make_guess = st.text_input("Make a guess: ", key="guess_input")
            try:
                guess = int(make_guess)
            except ValueError:
                st.write("Please enter a valid number.")
                continue

            you_win = check_guesses(guess, st.session_state.winning_number)
            if you_win:
                st.write(f"Congratulations! You guessed the number {st.session_state.winning_number}!")
                break
            else:
                max_guesses -= 1
                if max_guesses > 0:
                    st.write("Guess again.")
                    if max_guesses > 1:
                        st.write(f"You have {max_guesses} attempts remaining to guess the number.")
                    else:
                        st.write("You have 1 attempt remaining to guess the number.")

    # Exit gracefully if user runs out of attempts
    if max_guesses == 0:
        st.write(f"Sorry, but you've run out of guesses. The winning number was {st.session_state.winning_number}.")
    st.session_state.winning_number = 0

if __name__ == "__main__":
    game()
