from colorama import Fore, Style, init
from os import system, name
from time import sleep

# Initialize colorama to support colored text in the console
init(autoreset=True)


def clear_screen():
    """
    Clears the terminal screen for better readability.
    Works for both Windows and Unix-based systems.
    """
    system("cls" if name == "nt" else "clear")


# Dictionary to store book details in the library catalog
library_catalog = {}


def add_book():
    """
    Function to add a new book to the library catalog.
    It prompts the user for ISBN, title, and author details.
    """
    clear_screen()
    while True:
        # Request and process ISBN input
        isbn = input("Enter ISBN (numeric only): ").zfill(3).replace(" ", "")

        # Ensure ISBN is numeric
        if not isbn.isdigit():
            print(Fore.RED + "Error: ISBN must be numeric. Please try again.")
            continue

        # Ensure ISBN is unique in the catalog
        if isbn in library_catalog:
            print(
                Fore.RED
                + "Error: This book is already in the catalog. Please try again."
            )
            continue

        # Request and process book details
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()

        # Add the book to the library catalog
        library_catalog[isbn] = {"title": title, "author": author, "available": True}
        print(
            Fore.GREEN
            + f"Success: Book '{title}' by {author} added to the catalog with ISBN {isbn}."
        )

        # Check if the user wants to add another book
        another = input("Do you want to add another book? (y/n): ").lower()
        if another != "y":
            break


def check_out_book():
    """
    Function to check out a book from the library catalog.
    It ensures the book is available and marks it as borrowed.
    """
    clear_screen()
    while True:
        # Check if there are any books available for checkout
        available_books = [
            isbn for isbn, details in library_catalog.items() if details["available"]
        ]
        if not available_books:
            print(Fore.RED + "No books available for checkout.")
            sleep(2)
            break

        # Request and process ISBN input
        isbn = input("Enter ISBN to check out: ").zfill(3).replace(" ", "")

        # Validate the ISBN exists in the catalog
        if isbn not in library_catalog:
            print(Fore.RED + "Error: Book not found in the catalog. Please try again.")
            continue

        # Check if the book is already checked out
        if not library_catalog[isbn]["available"]:
            print(Fore.YELLOW + "Warning: The book is currently checked out.")
            continue

        # Mark the book as checked out
        library_catalog[isbn]["available"] = False
        print(
            Fore.GREEN
            + f"Success: Book '{library_catalog[isbn]['title']}' checked out successfully."
        )

        # Prompt to check out another book
        another = input("Do you want to check out another book? (y/n): ").lower()
        if another != "y":
            break


def check_in_book():
    """
    Function to check in a previously borrowed book.
    It ensures the book is in the catalog and currently marked as borrowed.
    """
    clear_screen()
    while True:
        # Check if there are any books currently borrowed
        borrowed_books = [
            isbn
            for isbn, details in library_catalog.items()
            if not details["available"]
        ]
        if not borrowed_books:
            print(Fore.RED + "No books borrowed for check-in.")
            sleep(2)
            break

        # Request and process ISBN input
        isbn = input("Enter ISBN to check in: ").zfill(3).replace(" ", "")

        # Validate the ISBN exists in the catalog
        if isbn not in library_catalog:
            print(Fore.RED + "Error: Book not found in the catalog. Please try again.")
            continue

        # Check if the book is already marked as available
        if library_catalog[isbn]["available"]:
            print(
                Fore.YELLOW + "Warning: The book is already available in the catalog."
            )
            continue

        # Mark the book as available
        library_catalog[isbn]["available"] = True
        print(
            Fore.GREEN
            + f"Success: Book '{library_catalog[isbn]['title']}' checked in successfully."
        )

        # Prompt to check in another book
        another = input("Do you want to check in another book? (y/n): ").lower()
        if another != "y":
            break


def list_books():
    """
    Function to display all books in the library catalog.
    It lists ISBN, title, author, and availability of each book.
    """
    clear_screen()
    if not library_catalog:
        print(Fore.RED + "No books to display.")
        sleep(2)
        return

    print(Fore.CYAN + "Library Catalog:")
    print("-" * 40)

    # Iterate and display each book's details
    for key, value in library_catalog.items():
        print(
            f"{Fore.MAGENTA}ISBN: {Fore.YELLOW}{key} {Style.RESET_ALL}| "
            f"{Fore.MAGENTA}Title: {Style.RESET_ALL}{value['title']} | "
            f"{Fore.MAGENTA}Author: {Style.RESET_ALL}{value['author']} | "
            f"{Fore.MAGENTA}Available: {Style.RESET_ALL}{'Yes' if value['available'] else 'No'}"
        )

    print("-" * 40)
    input("Press Enter to return to the main menu...")


# Main menu loop
while True:
    clear_screen()

    # Display the main menu
    print(Fore.CYAN + "Library Management System")
    print("-" * 30)
    print("1. Add Book")
    print("2. Check Out Book")
    print("3. Check In Book")
    print("4. List Books")
    print("5. Exit")
    print("-" * 30)

    # Request user input for menu choice
    choice = input("Enter your choice (1-5): ").strip()

    # Execute the corresponding function based on user choice
    if choice == "1":
        add_book()
    elif choice == "2":
        check_out_book()
    elif choice == "3":
        check_in_book()
    elif choice == "4":
        list_books()
    elif choice == "5":
        print(Fore.CYAN + "Exiting the program... Goodbye!")
        sleep(1)
        break
    else:
        print(Fore.RED + "Invalid choice. Please enter a number between 1 and 5.")
        sleep(2)
