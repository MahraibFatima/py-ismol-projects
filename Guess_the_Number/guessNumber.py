import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
    print("Thanks for playing!")