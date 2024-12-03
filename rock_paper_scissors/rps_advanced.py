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
    f"{Fore.MAGENTA}2. Each player chooses one of three options: Rock, Paper, or Scissors.",
    f"{Fore.MAGENTA}3. The winner is determined by the following rules:",
    f"{Fore.LIGHTGREEN_EX}   - Rock crushes Scissors (Rock wins).",
    f"{Fore.LIGHTGREEN_EX}   - Scissors cuts Paper (Scissors wins).",
    f"{Fore.LIGHTGREEN_EX}   - Paper covers Rock (Paper wins).",
    f"{Fore.MAGENTA}4. If both players choose the same option, the game is a tie.",
    f"{Fore.MAGENTA}5. The game can be played in multiple rounds.",
    f"{Fore.LIGHTYELLOW_EX}6. First to reach 3 points wins the game.{Style.RESET_ALL}",
)

# Available options in the game
OPTIONS = ["Rock", "Paper", "Scissors"]


# Functions to improve writing and display for the user
def clear_screen():
    """Clears the screen for better user experience."""
    system("cls" if name == "nt" else "clear")


def display_with_effects(
    text, text_delay=0.07, color=Fore.RESET, is_ASCII_art=False, ASCII_delay=0.01
):
    """Displays text or ASCII art with a typing or drawing animation effect."""
    delay = ASCII_delay if is_ASCII_art else text_delay
    stdout.write(color)
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(delay)
    stdout.write(Style.RESET_ALL)


def print_separator(color=Fore.YELLOW):
    """Prints a decorative separator."""
    print(color + "=" * 50)
    stdout.write(Style.RESET_ALL)


def display_title(title: str):
    """Displays a centered title with separators."""
    print_separator()
    print(Fore.CYAN + title.center(50))
    print_separator()


def show_final_results(user_score: int, computer_score: int):
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


# Dynamic functions to operate the program
def computer_choice() -> str:
    """Random selection for the computer and saving the appropriate ASCII art."""
    computer_choose = choice(OPTIONS)
    if computer_choose == "Rock":
        return computer_choose, rock_ascii
    elif computer_choose == "Paper":
        return computer_choose, paper_ascii
    else:
        return computer_choose, scissors_ascii


def user_choice(user_choose) -> str:
    """Validating the user's choice and storing the appropriate ASCII art for the correct selection."""
    if user_choose not in OPTIONS:
        return None, None
    if user_choose == "Rock":
        return user_choose, rock_ascii
    elif user_choose == "Paper":
        return user_choose, paper_ascii
    else:
        return user_choose, scissors_ascii


def compare_choices(user_choose, computer_choose) -> int:
    """Compares choices and returns the result."""
    if user_choose == computer_choose:
        return None  # Draw
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
        display_with_effects(
            "\nEnter your choice (rock, paper, scissors): ", color=Fore.CYAN
        )

        user_choose, user_ascii = user_choice(input().capitalize())
        computer_choose, computer_ascii = computer_choice()

        # Display the user's choice in ASCII ART
        if user_choose:
            print(f"\n{Fore.GREEN}You choose:")
            display_with_effects(user_ascii, color=Fore.GREEN, is_ASCII_art=True)
        else:
            display_with_effects("\nInvalid choice. Please try again.", color=Fore.RED)
            sleep(1)
            continue

        # Display the computer's choice in ASCII ART
        print(f"\n{Fore.RED}Computer choose:")
        display_with_effects(computer_ascii, color=Fore.RED, is_ASCII_art=True)

        result = compare_choices(user_choose, computer_choose)

        if result == 1:
            display_with_effects("\nYou won this round!", color=Fore.GREEN)
            user_score += 1
        elif result == 0:
            display_with_effects("\nComputer won this round.", color=Fore.RED)
            computer_score += 1
        else:
            display_with_effects("\nIt's a tie!", color=Fore.BLUE)

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
            display_with_effects(
                "Invalid input. Please type 'y' or 'n'.\n", color=Fore.RED
            )


def run_the_program():
    """Initializes the game, displays the start screen, and handles the game flow."""
    clear_screen()
    display_title("Welcome to Rock, Paper, Scissors")
    display_with_effects(
        "Press any key if you know the rules of the game. If you want help, type 'help': ",
        color=Fore.CYAN,
    )
    if input().lower() == "help":
        print()
        for line in rules:
            display_with_effects(line + "\n")
        sleep(2)
        display_with_effects(
            "\nIf you have understood the rules, get ready to play!",
            color=Fore.CYAN,
        )
    display_with_effects("\nPress Enter to begin your game...", color=Fore.GREEN)
    input()

    clear_screen()
    display_title("Starting Game")
    sleep(2)
    game()


# Start the program
run_the_program()
