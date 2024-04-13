import random
import time

# Get a number between 0 to 100
number = random.randint(0,100)

def User(name):
    print("{0} we are going to play a game. I am thinking a number between 0 to 100.".format(name))
    time.sleep(.8)
    print("Go Ahead. Guess!")

def pick():
    for i in range(1,10):
        guess = int(input("Guess: "))

        if guess<0 or guess>100:
            print("Silly Goose! That number isn't in the range!")
        elif guess<number:
            print("The guess of the number that you have enter is too low. Try Again!")
        elif guess>number:
            print("The guess of the number that you have enter is too high. Try Again!")
        
        elif guess==number:
            print("Good job {0}! You guessed my number in {1} guesses!".format(name, i))
            break

playagain = "yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    name = input("May I ask you for your name.\n")
    User(name)
    pick()
    playagain = input("Do you want to play again = ")

