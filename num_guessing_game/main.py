import random

class NumberGuessingGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)

    def user_input(self):
        while True:
            try:
                return int(input("Enter your number: "))
            except ValueError:
                print("Please enter a valid integer.")

    def play(self):
        while True:
            user_guess = self.user_input()
            if user_guess < self.target_number:
                print("Your guessing number is too low.")
            elif user_guess > self.target_number:
                print("Your guessing number is too high.")
            else:
                print("Your guessing number is correct!")
                break

# Game execution
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
