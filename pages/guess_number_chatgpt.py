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
    difficulty = st.selectbox("Choose a difficulty:", ["Not set", "Easy", "Hard"], key="difficulty_select")
    if difficulty.lower() == "hard":
        st.write("You have 5 attempts to guess the number.")
        st.session_state.max_guesses = 5
    elif difficulty.lower() == "easy":
        st.write("You have 10 attempts to guess the number.")
        st.session_state.max_guesses = 10
    else:
        st.write("Please choose a difficulty.")

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
        st.session_state.winning_number = random.randint(1, 100)

    if "max_guesses" not in st.session_state:
        st.session_state.max_guesses = 0

    st.session_state.max_guesses -= 1
    
    # Get the number of guesses based on difficulty
    difficulty_assignment()

    # Loop to take guesses
    while st.session_state.max_guesses > 0:
        make_guess = st.text_input("Make a guess:", key="guess_input")
        guess = int(make_guess) if make_guess.strip().isdigit() else None
        if guess is not None:
            you_win = check_guesses(guess, st.session_state.winning_number)
            if you_win:
                st.write("You got it! The answer was", st.session_state.winning_number)
                break
            else:
                st.session_state.max_guesses -= 1
                if st.session_state.max_guesses > 0:
                    st.write("Guess again.")
                    if st.session_state.max_guesses > 1:
                        st.write("You have", st.session_state.max_guesses, "attempts remaining to guess the number.")
                    else:
                        st.write("You have 1 attempt remaining to guess the number.")

# Run the game
if __name__ == "__main__":
    game()
