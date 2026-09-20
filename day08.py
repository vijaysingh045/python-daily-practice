import random


number = random.randint(1, 100)
attempts = 0

print("===== NUMBER GUESSING GAME =====")

print("Guess a number between 1 and 100")

while True:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too Low! Try again.")

    elif guess > number:
        print("Too High! Try again.")

    else:
        print("\nCorrect! 🎉")
        print("Number:", number)
        print("Attempts:", attempts)
        break