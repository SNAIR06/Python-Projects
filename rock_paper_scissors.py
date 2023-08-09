import random 
import os

def clear_console():
    os.system("clear") 

def game_beginning(game_choices):
    input("Welcome to Rock, Paper, Scissors! Press any key to continue. ")
    clear_console() 
    comp_choice = random.choice(game_choices)
    player_choice = input("Please choose rock, paper, or scissors: ").lower()
    clear_console()
    while player_choice not in game_choices:
        player_choice = input("Please choose rock, paper, or scissors: ").lower()
        clear_console()

def main():
    game_choices = ["rock", "paper", "scissors"]
    game_beginning(game_choices)

main()