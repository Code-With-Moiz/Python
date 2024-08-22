# Importing modules.
from random import randint
from math import log, ceil

# Function 1
def number_guessing_game():
    while True:
        try:
            lower_bound = int(input("Enter the lower bound (a positive integer): "))
            upper_bound = int(input("Enter the upper bound (a positive integer greater than lower bound): "))

            if lower_bound < 0 or upper_bound < 0:
                print("Please enter positive integers only.") 
                continue
            if upper_bound <= lower_bound:
                print("Upper bound should be greater than lower bound.")
                continue

            random_number = randint(lower_bound, upper_bound)
            number_of_guesses = ceil(log(upper_bound - lower_bound + 1, 2))
            print(f"You have {number_of_guesses} number of guesses. Good luck!")

            for count in range(1, number_of_guesses + 1):
                try:
                    guess = int(input("Guess a number: "))
                    if random_number == guess:
                        print(f"Congratulations! You guessed it right in {count} turns.")
                        return
                    elif random_number > guess:
                        print("Too low.")
                    else:
                        print("Too high.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            print(f"Sorry, you have used all your guesses. The correct number was {random_number}. Better luck next time!")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function 2
def main():
    while True:
        number_guessing_game()
        start_again = input("Do you want to play again? (yes, no): ").strip().lower()
        if start_again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()