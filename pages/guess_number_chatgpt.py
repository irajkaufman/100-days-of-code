import streamlit as st
from art import guess_number_logo
import random

# Function to check for difficulty level and return number of attempts
def difficulty_assignment():
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
        return "Too high."
    elif user_guess < correct_number:
        return "Too low."
    else:
        return "You got it!"

# Main game function
def game():
    st.markdown(guess_number_logo)
    st.markdown("Welcome to the Number Guessing Game!  \nI'm thinking of a number between 1 and 100.")

    # Initialize winning number and attempts if not already set
    if "winning_number" not in st.session_state:
        st.session_state.winning_number = random.randint(1, 100)

    if "max_guesses" not in st.session_state:
        st.session_state.max_guesses = 0

    st.session_state.max_guesses -= 1
    
    # Get the number of guesses based on difficulty
    max_guesses = difficulty_assignment()

    # Loop to take guesses
    while max_guesses > 0:
        chat_input = st.text_area("Chat:", value="Type your guess here...", height=100)
        if st.button("Send"):
            try:
                guess = int(chat_input.strip())
                feedback = check_guesses(guess, st.session_state.winning_number)
                st.write(feedback)
                if feedback == "You got it!":
                    st.write("The answer was", st.session_state.winning_number)
                    break
                else:
                    max_guesses -= 1
                    if max_guesses > 0:
                        st.write("Guess again.")
                        if max_guesses > 1:
                            st.write("You have", max_guesses, "attempts remaining to guess the number.")
                        else:
                            st.write("You have 1 attempt remaining to guess the number.")
            except ValueError:
                st.write("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    game()
