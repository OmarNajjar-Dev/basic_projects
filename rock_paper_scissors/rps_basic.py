import random

# Save Ascii in variables
rock_ascii = """   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)       """

paper_ascii = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)   """

scissors_ascii = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)       """

# Introduction
print("Welcome to the Rock, Paper, Scissors game:")
confirm = input("Press Enter to continue or type (Help) for the rules...").lower()

if confirm == "help":
    print(
        """\n
         ******Rules******
         1) You choose and the computer chooses
         2) Rock smashes Scissors -> Rock wins
         3) Scissors cut Paper -> Scissors wins
         4) Paper covers Rock -> Paper wins
         """
    )

user_choose = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
choices = ["Rock", "Paper", "Scissors"]

# Display user choice in ASCII
if user_choose not in choices:
    print(
        "Invalid choice. Please run the program again and choose rock, paper, or scissors"
    )

else:
    if user_choose == "Rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif user_choose == "Paper":
        print(f"\nYou chose:\n{paper_ascii}")
    else:
        print(f"\nYou chose:\n{scissors_ascii}")

    # Display computer choice in ASCII
    computer_choice = random.choice(choices)
    
    if computer_choice == "Rock":
        print(f"\nComputer choice:\n{rock_ascii}")
    elif computer_choice == "Paper":
        print(f"\nComputer choice:\n{paper_ascii}")
    else:
        print(f"\nComputer choice:\n{scissors_ascii}")

    if (
        (user_choose == "Rock" and computer_choice == "Scissors")
        or 
        (user_choose == "Paper" and computer_choice == "Rock")
        or 
        (user_choose == "Scissors" and computer_choice == "Paper")
    ):
        print(f"\nYou win. {user_choose} beats {computer_choice}")

    elif user_choose == computer_choice:
        print(f"\nYou lose. {computer_choice} beats {user_choose}")

    else:
        print("\nIt's a tie!")
