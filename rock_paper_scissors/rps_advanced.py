from colorama import Fore, init
import random
import time
import sys
import os

# Initialize colorama
init(autoreset=True)


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
    f"{Fore.YELLOW}Rock-Paper-Scissors Rules:",
    f"{Fore.CYAN}1. The game is played between two players.",
    f"{Fore.GREEN}2. Each player chooses one of three options: Rock, Paper, or Scissors.",
    f"{Fore.RED}3. The winner is determined by the following rules: ",
    f"{Fore.BLUE}   - Rock crushes Scissors (Rock wins).",
    f"{Fore.MAGENTA}   - Scissors cuts Paper (Scissors wins).",
    f"{Fore.GREEN}   - Paper covers Rock (Paper wins).",
    f"{Fore.YELLOW}4. If both players choose the same option, the game is a tie.",
    f"{Fore.CYAN}5. The game can be played in multiple rounds.",
    f"{Fore.RED}6. First to reach 3 points wins the game.",
)

computer_ascii = ""


def clear_screen():
    """Clears the screen for better user experience."""
    os.system("cls" if os.name == "nt" else "clear")


def slow_writing(text, delay=0.07, color=Fore.RESET):
    """Writes text to the screen with a typing animation effect."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def slow_writing_ascii(text):
    """Writes ASCII art to the screen with a typing animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


def print_separator():
    """Prints a decorative separator."""
    print(Fore.YELLOW + "=" * 50)


def display_title(title):
    """Displays a centered title with separators."""
    print_separator()
    print(Fore.CYAN + title.center(50))
    print_separator()


def run_the_program():
    """Runs the initial setup and guides the user through the rules if needed."""
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
        time.sleep(2)
        slow_writing(
            "\nIf you've read the rules enough, let's begin.\n", color=Fore.GREEN
        )
        input("\nPress Enter to start the game...")
    game()


def computer_choice():
    """Randomly selects and returns the computer's choice."""
    global computer_ascii
    computer_choose = random.choice(["Rock", "Paper", "Scissors"])
    if computer_choose == "Rock":
        computer_ascii = rock_ascii
    elif computer_choose == "Paper":
        computer_ascii = paper_ascii
    else:
        computer_ascii = scissors_ascii
    return computer_choose


def game():
    """Runs the main game loop."""
    clear_screen()
    display_title("Starting Game")
    time.sleep(2)
    computer_score = 0
    user_score = 0

    while True:
        clear_screen()
        display_title("Rock, Paper, Scissors")
        slow_writing("\nEnter your choice (rock, paper, scissors): ", color=Fore.CYAN)
        user_choose = input().capitalize()
        computer_choose = computer_choice()

        if user_choose not in ["Rock", "Paper", "Scissors"]:
            slow_writing("\nInvalid choice. Please try again.", color=Fore.RED)
            time.sleep(2)
            continue

        print(f"\n{Fore.GREEN}You choose: ")
        if user_choose == "Rock":
            slow_writing_ascii(rock_ascii)
        elif user_choose == "Paper":
            slow_writing_ascii(paper_ascii)
        elif user_choose == "Scissors":
            slow_writing_ascii(scissors_ascii)

        print(f"\n{Fore.YELLOW}Computer choose: ")
        slow_writing_ascii(computer_ascii)

        if user_choose == computer_choose:
            slow_writing("\nIt's a tie!", color=Fore.BLUE)
        elif (
            (user_choose == "Rock" and computer_choose == "Scissors")
            or (user_choose == "Paper" and computer_choose == "Rock")
            or (user_choose == "Scissors" and computer_choose == "Paper")
        ):
            slow_writing("\nYou won this round!", color=Fore.GREEN)
            user_score += 1
        else:
            slow_writing("\nComputer won this round.", color=Fore.RED)
            computer_score += 1

        print(
            f"\n{Fore.CYAN}Your score: {user_score} | Computer score: {computer_score}"
        )
        print_separator()  # Always after displaying results

        if computer_score == 3:
            display_title("Computer Wins!")
            break
        elif user_score == 3:
            display_title("You Win!")
            break
        else:
            input("\nPress Enter to proceed to the next round...")

    while True:
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay == "y":
            game()
        elif replay == "n":
            display_title("Thank You for Playing!")
            sys.exit()
        else:
            slow_writing("\nInvalid input. Please type 'y' or 'n'.", color=Fore.RED)


# Start the program
run_the_program()
