import random

print("what is your name?")
name = input()
secretNumber = random.randint(1, 20)
print("i thinking of a number between 1 and 20, guess it " + name)

guessCount = 0

while True:
    guessCount += 1
    print("take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("higher")
    elif guess > secretNumber:
        print("lower")
    elif guess == secretNumber:
        print("that's right")
        print("it takes " + name + " " + str(guessCount) + " guesses")
        break

    if guessCount >= 6:
        print("you loose")
        print("you used all of your guesses")
        break

