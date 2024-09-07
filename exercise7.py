# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    fixed_number = 42
    attempts = 5

    print("Guess a number between 1 and 100:")

    for attempt in range(1, attempts +1):
        guess = int(input("Enter your guess: "))

        if guess == fixed_number:
            print("Congratulations, you guessed correctly!")
            break

        elif guess < fixed_number:
            print("Guess is too low.")
        
        elif guess > fixed_number:
            print("Guess is too high")
        
        if attempt == attempts - 1:
            print("Last Chance!")
    else:
        print(f"Sorry, you failed to guess the correct number, {fixed_number}")


# Call the function
guess_number()

