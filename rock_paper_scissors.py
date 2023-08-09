import random as rng
import os

def clear_console():
    os.system("clear")

def game_beginning():
    input("Welcome to Rock, Paper, Scissors! Press any key to continue. ")
    clear_console()
    game_choices = ["rock", "paper", "scissors"]
    comp_choice = rng.choice(game_choices)
    player_choice = input("Please choose rock, paper, or scissors: ").lower()
    clear_console()

def main():
    game_beginning()

main()
