from colorama import Fore, Style, init
import os
import time

# Initialize colorama
init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


books = {}  # Dictionary to store books in the catalog


def Add():
    clear_screen()
    while True:
        book_ISBN = input("Enter ISBN (numeric only): ").replace(" ", "").zfill(3)

        # Ensure ISBN is numeric
        if not book_ISBN.isdigit():
            print(Fore.RED + "Error: ISBN must be numeric. Please try again.")
            continue

        # Check if the ISBN already exists
        if book_ISBN in books:
            print(
                Fore.RED
                + "Error: This book is already in the catalog. Please try again."
            )
            continue

        # Get book details
        book_title = input("Enter title: ").strip()
        book_author = input("Enter author: ").strip()

        # Add book to catalog
        books[book_ISBN] = [book_title, book_author, True]
        print(
            Fore.GREEN
            + f"Success: Book '{book_title}' by {book_author} added to the catalog with ISBN {book_ISBN}."
        )

        # Prompt to add another book
        another = input("Do you want to add another book? (y/n): ").lower()
        if another != "y":
            break


def Check_Out():
    clear_screen()
    while True:
        # Check if there are available books to borrow
        available_books = [isbn for isbn, details in books.items() if details[2]]
        if not available_books:
            print(Fore.RED + "No books available for checkout.")
            time.sleep(2)
            break

        check_out = input("Enter ISBN to check out: ").replace(" ", "").zfill(3)

        # If the book is not found in the catalog
        if check_out not in books:
            print(Fore.RED + "Error: Book not found in the catalog. Please try again.")
            continue

        # If the book is already checked out
        if not books[check_out][2]:
            print(Fore.YELLOW + "Warning: The book is currently checked out.")
            continue

        # Check out the book
        books[check_out][2] = False
        print(
            Fore.GREEN
            + f"Success: Book '{books[check_out][0]}' checked out successfully."
        )

        # Check again if any books are available
        available_books = [isbn for isbn, details in books.items() if details[2]]
        if not available_books:
            print(Fore.RED + "No more books available for checkout.")
            time.sleep(2)
            break

        # Prompt to check out another book
        another = input("Do you want to check out another book? (y/n): ").lower()
        if another != "y":
            break


def Check_In():
    clear_screen()
    while True:
        borrowed_books = [isbn for isbn, details in books.items() if not details[2]]
        if not borrowed_books:
            print(Fore.RED + "No books borrowed for check-in.")
            time.sleep(2)
            break

        check_in = input("Enter ISBN to check in: ").replace(" ", "").zfill(3)

        # If the book is not found in the catalog
        if check_in not in books:
            print(Fore.RED + "Error: Book not found in the catalog. Please try again.")
            continue

        # If the book is already available
        if books[check_in][2]:
            print(
                Fore.YELLOW + "Warning: The book is already available in the catalog."
            )
            continue

        # Check in the book
        books[check_in][2] = True
        print(
            Fore.GREEN
            + f"Success: Book '{books[check_in][0]}' checked in successfully."
        )

        # Prompt to check in another book
        another = input("Do you want to check in another book? (y/n): ").lower()
        if another != "y":
            break


def list_books():
    clear_screen()
    if not books:
        print(Fore.RED + "No books to display.")
        time.sleep(2)
        return

    print(Fore.CYAN + "Library Catalog:")
    print("-" * 40)

    # Display each book in the catalog with colorized fields
    for key, value in books.items():
        print(
            f"{Fore.MAGENTA}ISBN: {Fore.YELLOW}{key} {Style.RESET_ALL}| "
            f"{Fore.MAGENTA}Title: {Style.RESET_ALL}{value[0]} | "
            f"{Fore.MAGENTA}Author: {Style.RESET_ALL}{value[1]} | "
            f"{Fore.MAGENTA}Available: {Style.RESET_ALL}{'Yes' if value[2] else 'No'}"
        )

    print("-" * 40)
    input("Press Enter to return to the main menu...")


# Main menu loop
while True:
    clear_screen()

    # Display main menu
    print(Fore.CYAN + "Library Management System")
    print("-" * 30)
    print("1. Add Book")
    print("2. Check Out Book")
    print("3. Check In Book")
    print("4. List Books")
    print("5. Exit")
    print("-" * 30)

    choice = input("Enter your choice (1-5): ").strip()

    # Process user choice
    if choice == "1":
        Add()
    elif choice == "2":
        Check_Out()
    elif choice == "3":
        Check_In()
    elif choice == "4":
        list_books()
    elif choice == "5":
        print(Fore.CYAN + "Exiting the program... Goodbye!")
        time.sleep(1)
        break
    else:
        print(Fore.RED + "Invalid choice. Please enter a number between 1 and 5.")
        time.sleep(2)
