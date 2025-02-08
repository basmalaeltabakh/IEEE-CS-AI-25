import random

target = random.randint(1, 100)
tries = 5

for attempt in range(tries):
    guess = int(input(f" Attempt {attempt + 1}/{tries}: Enter your guess: "))

    if guess == target:
        print(" You guessed the correct number ")
        break
    elif guess < target:
        print(" Your guess is too low , try higer number ")
    else:
        print(" Your guess is too high , try lower number ")

    if attempt == tries - 1:
        print(f" Out of attempts ,  The correct number was: {target}")
