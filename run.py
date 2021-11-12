import random

#Start Game

play_game = True

while play_game:

    name = input("What is your name?").title()
    print("Hello " + name + "! Would you like to play Rock Paper Scissors? y/n ")

    answer = input().lower()

    if answer.lower() == "y":
        print("Learn how to play")
    elif answer.lower() == "n":
        print("Exit game")
        play_game = False
    else:
        print("Please enter y or n :)")
print("Thank you for playing. Hope to see you again ^8^ ")