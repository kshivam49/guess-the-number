import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if guess == random_number:
            print(f"Congratulation! You have guess the lucky number: {random_number}")
        elif guess>random_number:
            print("Lucky number is less than your guess")
        elif guess<random_number:
            print("Lucky number is more than your guess")

guess(100)


input('Press ENTER to exit')