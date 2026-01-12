import random

# Generate random number between 1 - 100
number = random.randint(1, 100)
atm = 0 # count the no. of attempts taken
guess = None
print("Random Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
while guess != number:
    guess = int(input("And now you guess, what no. it is ? : "))
    atm += 1
    if guess < number:
        print(" Low! Try again.")
    elif guess > number:
        print("High! Try again.")
    else:
        print(f"Congratulations! You guessed it in {atm} attempts.")
