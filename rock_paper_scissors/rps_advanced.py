from colorama import Fore, Style
from os import system, name
from sys import stdout
from time import sleep
from random import choice


# ASCII representations for Rock, Paper, Scissors
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_ascii = """   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_ascii = """  
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Game rules
rules = (
    f"{Fore.LIGHTCYAN_EX}Rock-Paper-Scissors Rules:",
    f"{Fore.MAGENTA}1. The game is played between two players.",
    f"{Fore.LIGHTGREEN_EX}2. Each player chooses one of three options: Rock, Paper, or Scissors.",
    f"{Fore.LIGHTRED_EX}3. The winner is determined by the following rules:",
    f"{Fore.BLUE}   - Rock crushes Scissors (Rock wins).",
    f"{Fore.BLUE}   - Scissors cuts Paper (Scissors wins).",
    f"{Fore.BLUE}   - Paper covers Rock (Paper wins).",
    f"{Fore.LIGHTRED_EX}4. If both players choose the same option, the game is a tie.",
    f"{Fore.LIGHTMAGENTA_EX}5. The game can be played in multiple rounds.",
    f"{Fore.YELLOW}6. First to reach 3 points wins the game.{Style.RESET_ALL}",
)

computer_ascii = ""  # To store the computer’s choice as ASCII art.
user_ascii = ""  # To store the user's choice as ASCII art.


# Functions to improve writing and display for the user.
def clear_screen():
    """Clears the screen for better user experience."""
    system("cls" if name == "nt" else "clear")


def slow_writing(text, delay=0.07, color=Fore.RESET):
    """Writes text to the screen with a typing animation effect."""
    stdout.write(color)
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(delay)
    stdout.write(Style.RESET_ALL)


def slow_writing_ascii(text):
    """Writes ASCII art to the screen with a typing animation effect."""
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(0.01)


def print_separator(color=Fore.YELLOW):
    """Prints a decorative separator."""
    print(color + "=" * 50)
    stdout.write(Style.RESET_ALL)


def display_title(title):
    """Displays a centered title with separators."""
    print_separator()
    print(Fore.CYAN + title.center(50))
    print_separator()


# Display the final results
def show_final_results(user_score, computer_score):
    """Displays the final results with a styled message."""
    clear_screen()
    if user_score > computer_score:
        display_title("Congratulations! You Win!")
    else:
        display_title("Computer Wins! Better Luck Next Time!")
    print(
        f"{Fore.CYAN}Final Score: {Fore.GREEN}You: {user_score} {Fore.RED}| Computer: {computer_score}"
    )
    print_separator()


# Dynamic functions to operate the program.
def computer_choice():
    """Random selection for the computer and saving the appropriate ASCII art."""
    global computer_ascii

    computer_choose = choice(["Rock", "Paper", "Scissors"])

    if computer_choose == "Rock":
        computer_ascii = rock_ascii
    elif computer_choose == "Paper":
        computer_ascii = paper_ascii
    else:
        computer_ascii = scissors_ascii
    return computer_choose


def user_choice(user_choose):
    """Validating the user's choice and storing the appropriate ASCII art for the correct selection."""
    global user_ascii
    if user_choose not in ["Rock", "Paper", "Scissors"]:
        return False
    if user_choose == "Rock":
        user_ascii = rock_ascii
    elif user_choose == "Paper":
        user_ascii = paper_ascii
    else:
        user_ascii = scissors_ascii
    return user_choose


def compare_choices(user_choose, computer_choose):
    """Compares choices and returns the result"""
    if user_choose == computer_choose:
        return  # Draw
    elif (
        (user_choose == "Rock" and computer_choose == "Scissors")
        or (user_choose == "Paper" and computer_choose == "Rock")
        or (user_choose == "Scissors" and computer_choose == "Paper")
    ):
        return 1  # User Won
    else:
        return 0  # User Lost


def game():
    """Compare the scores and provide the results."""
    computer_score = 0
    user_score = 0
    while True:
        clear_screen()
        display_title("Rock, Paper, Scissors")
        slow_writing("\nEnter your choice (rock, paper, scissors): ", color=Fore.CYAN)

        user_choose = input().capitalize()
        computer_choose = computer_choice()

        # Display the user's choice in ASCII ART
        if user_choice(user_choose):
            print(f"\n{Fore.GREEN}You choose:")
            slow_writing_ascii(user_ascii)
        else:
            slow_writing("\nInvalid choice. Please try again.", color=Fore.RED)
            sleep(2)
            continue

        # Display the computer's choice in ASCII ART
        print(f"\n{Fore.YELLOW}Computer choose:")
        slow_writing_ascii(computer_ascii)

        result = compare_choices(user_choose, computer_choose)

        if result == 1:
            slow_writing("\nYou won this round!", color=Fore.GREEN)
            user_score += 1
        elif result == 0:
            slow_writing("\nComputer won this round.", color=Fore.RED)
            computer_score += 1
        else:
            slow_writing("\nIt's a tie!", color=Fore.BLUE)

        print(
            f"\n{Fore.CYAN}Your score: {user_score} | Computer score: {computer_score}"
        )
        print_separator()

        if computer_score == 3 or user_score == 3:
            show_final_results(user_score, computer_score)
            break
        else:
            input("\nPress Enter to proceed to the next round...")

    # Play again
    while True:
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay == "y":
            game()
        elif replay == "n":
            display_title("Thank You for Playing!")
            quit()
        else:
            slow_writing("Invalid input. Please type 'y' or 'n'.\n", color=Fore.RED)


def run_the_program():
    """Displaying the start interface and running the game."""
    clear_screen()
    display_title("Welcome to Rock, Paper, Scissors")
    slow_writing(
        "Press any key if you know the rules of the game. If you want help, type 'help': ",
        color=Fore.CYAN,
    )
    if input().lower() == "help":
        print()
        for line in rules:
            slow_writing(line + "\n")
        sleep(2)
    slow_writing(
        "\nIf you have understood the rules, get ready to play!",
        color=Fore.LIGHTCYAN_EX,
    )
    slow_writing("\nPress Enter to begin your game...", color=Fore.GREEN)
    input()

    clear_screen()
    display_title("Starting Game")
    sleep(2)
    game()


# Start the program
run_the_program()
