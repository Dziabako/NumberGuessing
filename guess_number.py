import random

ongoing = True
number = random.randint(1, 100)
lives = 10

while ongoing:
    guess = int(input("Guess the number: "))
    if guess < number and lives > 1:
        print("Higher!")
        lives -= 1
        print("You have", lives, "lives left.")
    elif guess > number and lives > 1:
        print("Lower!")
        lives -= 1
        print("You have", lives, "lives left.")
    elif lives == 1:
        print("You lost! The number was:", number)
        ongoing = False
    else:
        print("Congratulations! You guessed the number!")
        ongoing = False
