import random

computer_guess = random.randint(1,100)
while True:
    user_guessing_number = int(input("Enter your guessing number :"))

    if user_guessing_number < computer_guess:
        print("your guessing number is too low")

    elif user_guessing_number > computer_guess:
        print("youer guessing number is too high")

    else:
        print("your select number is correct")
        break
