import random
import math

def play():
    """
    set rules and start to play
    """
    player = None

    choices = ['r','p','s']
    while player not in choices:
        player = input("Please enter your choice 'r' for Rock, 'p' for Paper or 's' for Scissors:\n").lower()

    computer = random.choice(choices)
    
    if player == computer:
        return (0,player,computer)
    if win(player, computer):
        return (1,player,computer)
    return (-1,player,computer)


def win(a, b):
    """
    the player won will return to be true
    r > s, s > p, p > r
    """
    if (a == 'r' and b == 's') or (a == 's' and b == 'p') or (a == 'p' and b == 'r'):
        return True
    return False


def player_win(n):
    """
    play with the computer until player wins 3 games
    """
    player_wins = 0
    wins_count = math.ceil(n/2)

    while player_wins < wins_count and player_wins < 3:
        result, player, computer = play()
        if result == 0:
            print("It's a tie.\n You have chosen {}. \n The computer has chosen {}.\n".format(player, computer))
        elif result == 1:
            player_wins += 1
            print("You won! ^^. \n You have chosen {}. \n The computer has chosen {}. \n".format(player, computer))
        else:
            print("You lost! ^^. \n You have chosen {}. \n The computer has chosen {}. \n".format(player, computer))
        print()
    



#Ask for player name and if they want to play the game or exit the game

play_game = True

while play_game:

    name = input("What is your name? \n").title()
    start_game = ("Hello " + name + "! Would you like to play Rock Paper Scissors? y/n ")

    print(start_game)

    answer = input().lower()
    answers = [ 'y','n']

    while answer not in answers:
        answer = input("\n Please enter 'y' or 'n' to start or exit the game :)").lower()

        if answer.lower() == "y":
            print("\t Play Rock-Paper-Scissors with computer to display a picture after 3 wins! \n")
            print("\t 'r' for Rock, 'p' for Paper, 's' for Scissors, 'q' for Quit \n ")
            player_win(5)

        elif answer.lower() == "n":
            print("Exit game")
            play_game = False
        
        else:
            print("Please enter y or n :)")


print("Thank you for playing. Hope to see you again ^8^ ")

