# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:54:14 2019

@author: luisf
"""

"""
09. rock, paper, scissors
"""
# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

import random
#foo = ['a', 'b', 'c', 'd', 'e']
#
#print(random.choice(foo))

# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.

options = ["stone", "paper", "scissors"]

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games

win_the_game = 3

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.

def machine_play(a):
    return(random.choice(a))

machine_choice = machine_play(options)

# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.

def user_play():
    a = input("Enter your choice: ")
    if a not in options:
            print("Not a valid option, try again ('stone', 'paper', 'scissors')")
    while a not in options:
        a = input("Enter your choice: ")
        if a not in options:
            print("Not a valid option, try again ('stone', 'paper', 'scissors')")
    return a

user_choice = user_play()

# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
 
def combat(mchoice,uchoice):
    if mchoice == uchoice:
        return 0
    elif uchoice == "stone":
        if mchoice == "scissors":
            return 2
        else:
            return 1
    elif uchoice == "paper":
        if mchoice == "stone":
            return 2
        else:
            return 1
    elif uchoice == "scissors":
        if mchoice == "paper":
            return 2
        else:
            return 1


# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated


#user_choice = user_play()
#machine_choice = machine_play(options)
#print("The machine choice is: ", machine_choice)
#the_game = combat(machine_choice, user_choice)

    
# Create two variables that accumulate the wins of each participant
machine_wins = 0
user_wins = 0

# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.
# Print by console the winner of the game based on who has more accumulated wins

machine_wins = 0
user_wins = 0
while machine_wins < win_the_game and user_wins < win_the_game:
    user_choice = user_play()
    machine_choice = random.choice(options)
    print("The machine choice is: ", machine_choice)
    
    the_game = combat(machine_choice, user_choice)
    if the_game == 1:
        machine_wins += 1
    elif the_game == 2:
        user_wins += 1
    else:
        print("Its a tie!! continue")
    
    print("\nUser wins: ", user_wins, "\nMachine wins: ", machine_wins)
    
    if machine_wins == 3:
        print("-------Sorry dude, better luck next time-------")
    elif user_wins == 3:
        print("-------Great! You win-------")     




