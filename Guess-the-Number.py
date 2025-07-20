import random

secret = random.randint(1, 10)
attempts = 0

print("🎮 Guess the Number Game 🎮")
print("I'm thinking of a number between 1 and 10.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
    elif guess < secret:
        print("Too low. Try again!")
    else:
        print("Too high. Try again!")
