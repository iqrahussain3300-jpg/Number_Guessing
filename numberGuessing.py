import random

# Generate a random number between 1 and 100
n = random.randint(1, 100)
number_of_guesses = 1
max_guesses = 9

print("🎲 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")
print(f"You have {max_guesses} chances.\n")

while number_of_guesses <= max_guesses:
    a = int(input("Enter your guess: "))
    
    if a < n:
        print("Too small!")
    elif a > n:
        print("Too big!")
    else:
        print("🎉 You won!")
        print(f"You took {number_of_guesses} guesses.")
        break

    print(max_guesses - number_of_guesses, "guesses left\n")
    number_of_guesses += 1

if number_of_guesses > max_guesses:
    print(f"Game Over 😢 The correct number was {n}.")
