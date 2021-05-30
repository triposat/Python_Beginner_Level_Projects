# Import random module
import random

# Function for Computer Guess


def comp_guess(low_val, high_val, randnum, count=0):
    if high_val >= low_val:  # When high_val greater than low_val
        guess = low_val+(high_val-low_val)//2
        if guess == randnum:  # if guess is equals randnum then return the count
            return count
        elif guess > randnum:  # if guess is greater than randnum the increase the count and call the function recursively again
            count += 1
            return comp_guess(low_val, guess-1, randnum, count)
        else:
            count += 1
            return comp_guess(guess+1, high_val, randnum, count)


# Driver Function
randnum = random.randint(1, 100)  # Store any random number b/w 1 and 100
count = 0  # Initialize count to 0
guess = 0  # Initialize guess to 0
while guess != randnum:  # Loop till we guess the number
    # Taking input from the user
    guess = int(input("\nPlease Guess the No. b/w 1 & 100: "))
    if guess > randnum:  # Check whether number is Greater or not.
        print("You Guess Higher No.")
    elif guess < randnum:  # Check whether number is Lower or not.
        print("You Guess Lower No.")
    else:
        print("Great!, You guess the No.")
    count += 1  # Increase count
# Display the Final Result
print(f"You took: {count} Chances!")
# Call comp_guess function
print(f"Computer took: {comp_guess(0,100,randnum)} Chances!")
