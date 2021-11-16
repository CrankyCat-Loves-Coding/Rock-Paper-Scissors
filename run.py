import random
import math
import time


def welcome():
    """
    add welcome page
    display game name and welcome to play
    """
    print("──────────────────────────────────────────────────")
    print("─████████████████───██████████████─██████████████─")
    print("─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─")
    print("─██░░████████░░██───██░░██████░░██─██░░██████████─")
    print("─██░░██────██░░██───██░░██──██░░██─██░░██─────────")
    print("─██░░████████░░██───██░░██████░░██─██░░██████████─")
    print("─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─")
    print("─██░░██████░░████───██░░██████████─██████████░░██─")
    print("─██░░██──██░░██─────██░░██─────────────────██░░██─")
    print("─██░░██──██░░██████─██░░██─────────██████████░░██─")
    print("─██░░██──██░░░░░░██─██░░██─────────██░░░░░░░░░░██─")
    print("─██████──██████████─██████─────────██████████████─")
    print("──────────────────────────────────────────────────")
    print("─────────────────Come─and─Play────────────────────")
    print("───────────────────(^.^)YYa!!─────────────────────\n")


def start():
    """
    the program will first obtain player's name
    then greet to the player
    game starts when player enter y
    game exit when player enter n
    """
    # obtain play's name and greet to the player
    # ask to start or exit the game
    name = input("What is your name? \n").title()
    print("\nHello " + name + "!ヽ(^o^)丿\n")
    time.sleep(1)
    print("Would you like to play Rock Paper Scissors?\n")
    time.sleep(1)
    print("Please enter 'y' for Yes and 'n' for No:\n")

    # start game
    play_game = True

    while play_game:
        # check input y and n
        # if input other than y or n
        # the program will ask the player to enter either y or n
        answer = input().lower()
        answers = ['y', 'n']

        while answer not in answers:
            answer = input("\nEnter 'y' or 'n' to start or exit the game :)\n")
            answer = answer.lower()
        # game start if y entered
        if answer.lower() == "y":
            print("\nPlay Rock-Paper-Scissors with computer to display a picture after 3 wins! ")
            print("\n'r' for Rock, 'p' for Paper, 's' for Scissors \n ")
            player_win(5)
        # exit game if n entered
        elif answer.lower() == "n":
            print("Exit game")
            print("Thank you for playing. Hope to see you again ^8^ ")
            play_game = False
        else:
            print("Please enter y or n :)")


def play():
    """
    set rules and start to play
    """
    player = None

    choices = ['r', 'p', 's']
    while player not in choices:
        player = input("Enter 'r' for Rock,'p' for Paper,'s' for Scissors\n")
        player = player.lower()

    computer = random.choice(choices)
    if player == computer:
        return (0, player, computer)
    if win(player, computer):
        return (1, player, computer)
    return (-1, player, computer)


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
    computer prints partial image each time player wins 
    """
    player_wins = 0
    wins_count = math.ceil(n/2)

    while player_wins < wins_count and player_wins < 3:
        result, player, computer = play()
        if result == 0:
            print("It's a tie!  (￣o￣).zZ ")
            print("You have chosen {}.".format(player))
            print("The computer has chosen {}.".format(computer))
        elif result == 1:
            player_wins += 1
            print("You won!  (｡♥‿♥｡) ")
            print("You have chosen {}.".format(player))
            print("The computer has chosen {}.".format(computer))
            if player_wins == 1:
                print('There is your reward! (づ｡◕‿‿◕｡)づ \n')
                print("────────────────────██████──────────")
                print("──────────────────██▓▓▓▓▓▓██────────")
                print("────────────────██▓▓▓▓▒▒▒▒██────────")
                print("────────────────██▓▓▒▒▒▒▒▒██────────")
                print("──────────────██▓▓▓▓▒▒▒▒██──────────")
                print("──────────────██▓▓▒▒▒▒▒▒██──────────")
                print("────────────██▓▓▓▓▒▒▒▒▒▒██──────────")
                print("────────────████▒▒████▒▒██──────────")
                print("────────────██▓▓▒▒▒▒▒▒▒▒██──────────")
            elif player_wins == 2:
                print('There is your reward! (づ｡◕‿‿◕｡)づ \n')
                print("──────────██────▒▒────▒▒██──────────")
                print("──────────████──▒▒██──▒▒██──────────")
                print("──────────██────▒▒────▒▒██──────────")
                print("──────────██▒▒▒▒▒▒▒▒▒▒▒▒██──────────")
                print("──────────████████████▒▒▒▒██────────")
                print("────────██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──────")
                print("──────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██────")
                print("────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██──")
                print("──██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██")
            elif player_wins == 3:
                print("You won 3 times! There is your reward! (づ｡◕‿‿◕｡)づ \n")
                print("────────────────────██████──────────")
                print("──────────────────██▓▓▓▓▓▓██────────")
                print("────────────────██▓▓▓▓▒▒▒▒██────────")
                print("────────────────██▓▓▒▒▒▒▒▒██────────")
                print("──────────────██▓▓▓▓▒▒▒▒██──────────")
                print("──────────────██▓▓▒▒▒▒▒▒██──────────")
                print("────────────██▓▓▓▓▒▒▒▒▒▒██──────────")
                print("────────────████▒▒████▒▒██──────────")
                print("────────────██▓▓▒▒▒▒▒▒▒▒██──────────")
                print("──────────██────▒▒────▒▒██──────────")
                print("──────────████──▒▒██──▒▒██──────────")
                print("──────────██────▒▒────▒▒██──────────")
                print("──────────██▒▒▒▒▒▒▒▒▒▒▒▒██──────────")
                print("──────────████████████▒▒▒▒██────────")
                print("────────██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──────")
                print("──────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██────")
                print("────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██──")
                print("──██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██")
                print("██▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██")
                print("██▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██")
                print("██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██")
                print("──████▐▌▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌▐▌████──")
                print("────██▐▌▐▌▌▌▌▌▌▌▌▌▐▌▐▌▐▌▐▌▌▌▐▌██────")
                print("────██▌▌▐▌▐▌▌▌▐▌▌▌▌▌▐▌▌▌▌▌▌▌▌▌██────")
                print("──────██▌▌▐▌▐▌▐▌▐▌▐▌▐▌▐▌▌▌▌▌██──────")
                print("──────██▐▌▐▌▐▌████████▐▌▌▌▌▌██──────")
                print("────────██▒▒██────────██▒▒██────────")
                print("────────██████────────██████────────\n")
                print("Would you like to play again?\n")
                print("Enter 'y' to continue \n")
                print("Enter 'q' and then 'n' to exit the game \n")
            else:
                print()
        else:
            print("You lost! o_O||  ")
            print("You have chosen {}.".format(player))
            print("The computer has chosen {}.".format(computer))
        print()

def main():
    """
    Run all program functions
    """
    welcome()
    start()
    

if __name__ == "__main__":
    main()