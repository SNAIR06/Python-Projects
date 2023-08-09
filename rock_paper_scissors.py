import random 
import os

def clear_console():
    os.system("clear") 

def game_beginning(game_choices):
    input("Welcome to Rock, Paper, Scissors! Press Enter to continue. ")
    clear_console() 
    
    player_choice = input("Please choose rock, paper, or scissors: ").lower()
    clear_console()
    
    while player_choice not in game_choices:
        player_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
        clear_console()
    
    comp_choice = random.choice(game_choices)  # Move computer choice here
    return player_choice, comp_choice

def find_winner(player_choice, comp_choice):
    if player_choice == "rock":
        if comp_choice == "rock":
            input("DRAW! Press any key to play again: ")
        elif comp_choice == "paper":
            input("YOU LOST! Press any key to play again: ")
        elif comp_choice == "scissors":
            input("YOU WON! Press any key to play againL: ")
def main():
    game_choices = ["rock", "paper", "scissors"]
    player_choice, comp_choice = game_beginning(game_choices) 
    
    find_winner(player_choice, comp_choice)

main()

