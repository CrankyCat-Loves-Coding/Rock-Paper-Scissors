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
    print("───────────────Rock─Paper─Scissors────────────────")
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
            print("▒█▀▀█ ▒█░▒█ ▒█░░░ ▒█▀▀▀ ▒█▀▀▀█ ")
            print("▒█▄▄▀ ▒█░▒█ ▒█░░░ ▒█▀▀▀ ░▀▀▀▄▄ ")
            print("▒█░▒█ ░▀▄▄▀ ▒█▄▄█ ▒█▄▄▄ ▒█▄▄▄█ ")
            print("────────────────────────────────────────────────────────\n")
            time.sleep(1)
            print("Rock Paper Scissors (RPS) is popular all over the world.\n")
            time.sleep(1)
            print("The rules to play are pretty simple.\n")
            time.sleep(1)
            print("The computer randomly chooses Rock, Paper or Scissors.\n")
            time.sleep(1)
            print("The player can enter \n‘r’ for Rock, \n‘p’ for Paper or" +
                  "\n‘s’ for Scissors to play against the computer.\n")
            time.sleep(1)
            print("The outcome of the game is determined by 3 simple rules:\n")
            time.sleep(1)
            print("Rock wins against scissors.")
            print("Scissors win against paper.")
            print("Paper wins against rock.\n")
            time.sleep(2)
            print("The computer displays a puzzle " +
                  "each time the player wins.\n")
            time.sleep(1)
            print("Once the player has won 3 times, " +
                  "the computer displays a full image.\n")
            time.sleep(1)
            print("Let's play and good luck! ─=≡Σ(((つ•̀ω•́)つ \n")

            player_win(5)
        # exit game if n entered
        elif answer.lower() == "n":
            print("Exit game")
            print("Thank you for playing. Hope to see you again ^8^ \n")
            print("╭━━━━┳╮╱╱╱╱╱╱╱╭╮╱╱╭╮╱╱╭╮")
            print("┃╭╮╭╮┃┃╱╱╱╱╱╱╱┃┃╱╱┃╰╮╭╯┃")
            print("╰╯┃┃╰┫╰━┳━━┳━╮┃┃╭╮╰╮╰╯╭┻━┳╮╭╮")
            print("╱╱┃┃╱┃╭╮┃╭╮┃╭╮┫╰╯╯╱╰╮╭┫╭╮┃┃┃┃")
            print("╱╱┃┃╱┃┃┃┃╭╮┃┃┃┃╭╮╮╱╱┃┃┃╰╯┃╰╯┃")
            print("╱╱╰╯╱╰╯╰┻╯╰┻╯╰┻╯╰╯╱╱╰╯╰━━┻━━╯")
            print("╭━━╮")
            print("┃╭╮┃")
            print("┃╰╯╰┳╮╱╭┳━━╮")
            print("┃╭━╮┃┃╱┃┃┃━┫")
            print("┃╰━╯┃╰━╯┃┃━┫")
            print("╰━━━┻━╮╭┻━━╯")
            print("╱╱╱╱╭━╯┃")
            print("╱╱╱╱╰━━╯")
            play_game = False
        else:
            print("Please enter y or n :)")


def play():
    """
    set rules
    the computer randomly choose r, p and s.
    validate player input and display message for unexpected answers
    asign value 0 for a tie
    otherwise asign 1 to player for winning
    and assign -1 for losing
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


def win(player, opponent):
    """
    the player wins return to be true
    winning condition as r > s, s > p, p > r
    """
    if (player == 'r' and opponent == 's'):
        return True
    elif(player == 's' and opponent == 'p'):
        return True
    elif(player == 'p' and opponent == 'r'):
        return True
    else:
        return False


def player_win(n):
    """
    If the player wins, the computer displays a message and a partial image.
    Once the player has won 3 times, the computer displays a full image.
    Then the player is asked if they wish to replay the game or exit the game.
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
                print("Enter any key and then 'n' to exit the game \n")
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
