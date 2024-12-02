import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Currency exchange rates
exchange_rates = {"USD": 1.0, "EUR": 0.85, "EGP": 30.9, "RMB": 6.5}
dollar = r""" 
   ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
"""


def clear_terminal():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def display_main_menu():
    """Displays the main menu with available exchange rates."""
    clear_terminal()
    print(f"Welcome to currency conversion:\n\n {Fore.GREEN}{dollar} \n")
    print("_" * 80 + "\n")
    print("Available Exchange Rates:")
    for currency, rate in exchange_rates.items():
        print(f"  - {currency}: {rate}")
    print("\n")


def get_currency_input(prompt):
    """Prompts the user to input a valid currency."""
    while True:
        currency = input(prompt).upper()
        if currency in exchange_rates:
            return currency
        print(Fore.RED + "Invalid currency. Please try again.")


def get_amount_input(prompt):
    """Prompts the user to input a valid amount."""
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            print("Amount must be positive. Please try again.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numeric value.")


def perform_conversion():
    """Handles the currency conversion logic."""
    display_main_menu()

    # Get the source currency and amount
    source_currency = get_currency_input("Choose a currency to convert from: ")
    amount = get_amount_input(f"Enter the amount in {source_currency}: ")
    confirm = input(f"You entered {amount} {source_currency}. Confirm? (Y/N): ").upper()

    if confirm != "Y":
        print(Fore.YELLOW + "Transaction canceled. Returning to main menu...")
        time.sleep(2)
        return

    clear_terminal()
    display_main_menu()

    # Get the target currency
    target_currency = get_currency_input("Choose a currency to convert to: ")

    # Calculate and display the conversion result
    print(Fore.CYAN + "Processing your request... Please wait.\n")
    time.sleep(2)
    exchange_rate = exchange_rates[target_currency] / exchange_rates[source_currency]
    converted_amount = round(amount * exchange_rate, 2)

    print(
        f"{Fore.YELLOW} Exchange Rate: 1 {source_currency} = {round(exchange_rate, 2)} {target_currency}"
    )
    print(
        f"{Fore.YELLOW} {amount} {source_currency} is equal to {converted_amount} {target_currency}\n"
    )

    # Confirm the transaction
    if (
        input(
            f"{Fore.RED}Do you accept this transaction? (Y/N): {Style.RESET_ALL}"
        ).upper()
        != "Y"
    ):
        print(Fore.RED + "Transaction canceled.\n")
        return

    print(Fore.GREEN + "Transaction completed successfully.\n")


def main():
    """Main function to start the program."""
    while True:
        perform_conversion()
        if input("Do you want to perform another conversion? (Y/N): ").upper() != "Y":
            print("Thank you for using the currency converter. Goodbye!")
            break


if __name__ == "__main__":
    main()
