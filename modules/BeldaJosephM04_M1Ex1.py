"""

Author:  Joseph Belda
Date written: 2/10/25
Assignment:   Assignment Part I
Short Desc:   This program will ask the user to give a number to the program.
Then the program will show the prime numbers and the ones that aren't prime numbers.

Note for prime numbers:
Example if the user puts 10. It'll show 10 numbers that are either prime or not.
2 is a prime number because it only be divided by 1 and the number itself.
4 isn't a prime because it can be divided by 2. 
The way you can think of this if the number has more
divisible numbers than 1 and the number itself, then it can't be a prime number.

"""

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to square root of num
        if num % i == 0:
            return False
    return True

# Main program
def main():
    # Get input from the user
    user_input = int(input("Enter a number: "))
    
    # Populate a list with integers from 2 to the entered number
    numbers = list(range(2, user_input + 1))
    
    # Loop through the list and check each number
    for num in numbers:
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

# Run the program
main()
