from colorama import Fore, Style
import random
import time
import sys 
import os


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
    f"{Fore.RED}6. The player with the most wins after the set number of rounds is the overall winner.{Style.RESET_ALL}"
)
computer_ascii = """ """

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def slow_writing(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)

def slow_writing_ascii(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01) 

def run_the_program():
    slow_writing ("Welcome to Rock, Paper, Scissors game")
    time.sleep(2)
    slow_writing ("\nPress any key if you know the rules of the game. If you want help, type 'help': ")
    if input().lower() == "help":
       print()
       for line in rules:
           sys.stdout.write (line + "\n")
           sys.stdout.flush()
           time.sleep (0.1)
       time.sleep (3)
       slow_writing ("\nIf you've read the rules enough, let's begin.\n")
       time.sleep (0.5)
       input ("Press any key to continue...")
       game()

def computer_choice():
     global computer_ascii
     computer_choice = random.choice(["Rock", "Paper", "Scissors"])

     if computer_choice == "Rock":
         computer_ascii = rock_ascii
        
     elif computer_choice == "Paper":
         computer_ascii = paper_ascii

     else:
         computer_ascii = scissors_ascii

     return computer_choice  

def game():
    clear_screen()
    print ("Starting game .......")
    time.sleep(3)
    computer_score = 0
    user_score = 0

    while True:
        # The computer's choice and the user's choice
        clear_screen()
        slow_writing ("Enter your choice (rock, paper, scissors): ")
        user_choose = input().capitalize()
        computer_choose = computer_choice()

        # Print the user's choice and the computer's choice in ASCII format
        if user_choose == "Rock":
            print ("\nYou choose: \n")
            slow_writing_ascii (rock_ascii)
            slow_writing_ascii (f"\nComputer choose: \n{computer_ascii}")

        elif user_choose == "Paper":
            print ("\nYou choose: \n")
            slow_writing_ascii (paper_ascii)
            slow_writing_ascii (f"\nComputer choose: \n{computer_ascii}")

        elif user_choose == "Scissors":
            print ("\nYou choose: \n")
            slow_writing_ascii (scissors_ascii)
            slow_writing_ascii (f"\nComputer choose: \n{computer_ascii}")

        else:
            print ("Invalid choice. Try again")
            time.sleep(2)
            continue

        # Calculate the points and give the results
        if user_choose == computer_choose:
            print ("\nIt's a tie")
        
        elif( 
            (user_choose == "Rock" and computer_choose == "Scissors")
            or
            (user_choose == "Paper" and computer_choose == "Rock")
            or 
            (user_choose == "Scissors" and computer_choose == "Paper")
            ):

            print ("\nYou won this round.")
            user_score += 1

        else:
            print ("\nComputer won this round.")
            computer_score += 1

        print (f"Your score is: {user_score}")
        print (f"Computer score is: {computer_score}")

        # Give the final results
        if computer_score == 3:
            slow_writing ("\nComputer reached to 3 points before you! Computer Win.")
            break
        elif user_score == 3:
            slow_writing ("\nYou reached to 3 points before the computer! You Win.")
            break
        else: 
            input ("\nPress any key to move to the next round . . .")

    while True:
        if input("\nDo you want to play again? y/n: ").lower() == "y":
            clear_screen()
            game()
        else:
            quit()

run_the_program()