import streamlit as st
import random

class NumberGuessingGame:
    def __init__(self):
        if 'target_number' not in st.session_state:
            st.session_state.target_number = random.randint(1, 100)
        if 'attempts' not in st.session_state:
            st.session_state.attempts = 0

    def guess(self, user_input):
        st.session_state.attempts += 1
        if user_input < st.session_state.target_number:
            return "Your guessing number is too low."
        elif user_input > st.session_state.target_number:
            return "Your guessing number is too high."
        else:
            return f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts."

    def reset_game(self):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.success("Game has been reset!")

# Streamlit UI
st.title("🎯 Number Guessing Game")

game = NumberGuessingGame()

user_guess = st.number_input("Enter a number between 1 and 100:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    result = game.guess(user_guess)
    st.write(result)

if st.button("Reset Game"):
    game.reset_game()
