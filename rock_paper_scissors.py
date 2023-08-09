import random as rng
import os

def clear_console():
    os.system("clear")

input("Welcome to Rock, Paper, Scissors! Press any key to continue. ")

clear_console()

game_choices = ["rock", "paper", "scissors"]

comp_choice = rng.choice(game_choices)

print(comp_choice)
