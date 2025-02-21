"""

Author:  Joseph Belda
Date written: 2/17/25
Assignment:   Assignment Part II
Short Desc: A number guessing game where the user tries to guess a random number 
between 1 and 100. The program provides hints if the guess is too high 
or too low, handles invalid inputs, and allows the player to play multiple 
rounds. The game continues until the correct number is guessed, and the 
player can choose to play again or exit.
"""






import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    while True:
        try:
            # Get the user's guess
            guess = int(input("Guess a number between 1 and 100: "))
            
            # Check if guess is too high or too low
            if guess > number:
                print("Too high, try again.")
            elif guess < number:
                print("Too low, try again.")
            else:
                print(f"Congratulations! You guessed the number {number} correctly!")
                play_again = input("Would you like to play again? (yes/no): ").lower()
                if play_again == 'yes':
                    # Generate new random number and continue game
                    number = random.randint(1, 100)
                    continue
                else:
                    print("Thanks for playing!")
                    break
                    
        except ValueError:
            print("Please enter a valid number.")

# Start the game
if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    number_guessing_game()
