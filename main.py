#guessing game
import random
print("Welcome to the guessing game.")
print("I am thinking between a number from 1 to 10")

secret_number=random.randint(1,10)
attempts=0

while True:
    guess=input("Enter your answer:")

    if not guess.isdigit():
        print("Please enter a valid number")
        continue
    guess=int(guess)
    attempts+=1
    if guess < secret_number:
        print("Too Low!Try again")
    elif guess > secret_number:
        print("Too high!Try again")
    else:
       print(f"Congrats!You guessed it in {attempts}attempts!")
       break




