import random

def play():
    """
    set rules and start to play
    """

    player = input().lower()
    computer = random.choice(['r','p','s'])
    
    if player == computer:
        return "You and the computer have both chosen {}. It's a tie.".format(computer)
    if win(player, computer):
        return "You have chosen {} \n the computer has chosen {}.\n You won! \n".format(player, computer)
    return "You have chosen {} \n the computer has chosen {}.\n You lost! \n".format(player, computer)


def win(a, b):
    if (a == 'r' and b == 's') or (a == 's' and b == 'p') or (a == 'p' and b == 'r'):
        return True
    return False


#Ask for player name and if they want to play the game or exit the game

play_game = True

while play_game:

    name = input("What is your name? \n").title()
    print("Hello " + name + "! Would you like to play Rock Paper Scissors? y/n ")

    answer = input().lower()

    if answer.lower() == "y":
        print("\t Play Rock-Paper-Scissors with computer to display a picture after 3 wins! \n")
        print("\t 'r' for Rock, 'p' for Paper, 's' for Scissors, 'q' for Quit \n ")
        print(play())

    elif answer.lower() == "n":
        print("Exit game")
        play_game = False
    else:
        print("Please enter y or n :)")

print("Thank you for playing. Hope to see you again ^8^ ")

