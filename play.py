# rock paper scissor lizard spock or rock paper scissor
from time import sleep as s  # for suspense
from random import randint as r  # for AI choice


def normal_game():
    print("let's play rock paper scissor")
    choice = ["rock", "paper", "scissor"]
    s(1)
    print(" 1 for rock \n 2 for paper \n 3 for scissor")
    playerchoice = input("rock, paper, or scissor?: ")
    if 0 < int(playerchoice) <= 3:  # verify the right choice
        init = True
    else:
        init = False
        print("invalid choice")

    while not init:
        playerchoice = input("rock, paper or scissor?: ")
        if 0 < int(playerchoice) <= 3:
            init = True
        else:
            init = False
            print("invalid choice")

    player = choice[int(playerchoice) - 1]
    ai = r(0, 2)
    if ai == 0:
        ai = "rock"
    elif ai == 1:
        ai = "paper"
    else:
        ai = "scissor"
    s(1)  # a little bit of suspense
    print("1")
    s(1)
    print("2")
    s(1)
    print("3")
    s(1)

    if player == ai:
        print("it's a tie")
    elif player == "rock" and ai == "scissor":
        print("you wins")
    elif player == "paper" and ai == "rock":
        print("you wins")
    elif player == "scissor" and ai == "paper":
        print("you wins")
    else:
        print("Loser")
    # rock paper scissor


def variant():
    print("let's play rock paper scissor lizard spock")
    choice = ["rock", "paper", "scissor", "lizard", "spock"]
    s(1)
    print(" 1 for rock \n 2 for paper \n 3 for scissor \n 4 for lizard \n 5 for spock")
    playerchoice = input("rock, paper, scissor, lizard, or spock?: ")
    if 0 < int(playerchoice) <= 5:  # verify the right choice
        init = True
    else:
        init = False
        print("invalid choice")

    while not init:
        playerchoice = input("rock, paper, scissor, lizard, or spock?: ")
        if 0 < int(playerchoice) <= 5:
            init = True
        else:
            init = False
            print("invalid choice")

    player = choice[int(playerchoice) - 1]
    ai = r(0, 4)
    if ai == 0:
        ai = "rock"
    elif ai == 1:
        ai = "paper"
    elif ai == 2:
        ai = "scissor"
    elif ai == 3:
        ai = "lizard"
    else:
        ai = "spock"
    s(1)  # a little bit of suspense
    print("1")
    s(1)
    print("2")
    s(1)
    print("3")
    s(1)
    if player == ai:
        print("it's a tie")
    elif player == "rock" and ai == "scissor":
        print("you wins")
    elif player == "rock" and ai == "lizard":
        print("you wins")
    elif player == "paper" and ai == "rock":
        print("you wins")
    elif player == "paper" and ai == "spock":
        print("you wins")
    elif player == "scissor" and ai == "paper":
        print("you wins")
    elif player == "scissor" and ai == "lizard":
        print("you wins")
    elif player == "lizard" and ai == "spock":
        print("you wins")
    elif player == "lizard" and ai == "paper":
        print("you wins")
    elif player == "spock" and ai == "rock":
        print("you wins")
    elif player == "spock" and ai == "scissor":
        print("you wins")
    else:
        print("Loser")
    # rock paper scissor lizard spock


def main():
    choice = input("what you want to play?: ")
    if choice == "1":
        normal_game()
    elif choice == "2":
        variant()
    else:
        print("invalid choice")
        main()


if __name__ == "__main__":
    print("welcome to the rock paper scissor game")
    print("put 1 for normal game \nput 2 for variant with lizard and spock")
    main()
    play = input("Do you want to play again? Y/N: ").upper()

    while play == "Y":
        main()
        play = input("Do you want to play again? Y/N: ").upper()
