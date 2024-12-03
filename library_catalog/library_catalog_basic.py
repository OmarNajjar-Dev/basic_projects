import os
import time


def clear_screen():
    """Clear the terminal screen for better readability"""
    os.system("cls" if os.name == "nt" else "clear")


library_catalog = {}  # Dictionary to store books in the catalog


def add_book():
    """Function to add a book to the catalog"""
    clear_screen()
    isbn = input("Enter ISBN: ").zfill(3).replace(" ", "")

    # Check if the ISBN is a number
    if not isbn.isdigit():
        print("That is not a number.")
        time.sleep(2)
        print()

    # Check if the book already exists
    elif isbn in library_catalog:
        print("This book is already in the catalog.")
        time.sleep(2)

    else:
        # Add the book details
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        library_catalog[isbn] = {"title": title, "author": author, "available": True}
        print(
            f"Book '{library_catalog[isbn]['title']}' by {library_catalog[isbn]['author']} added to the catalog with ISBN {isbn}."
        )

        # Ask if the user wants to add another book
        another = input("Do you want to add another book? (y/n): ").lower()
        if another == "y":
            clear_screen()
            add_book()


def check_out_book():
    """Function to check out a book from the catalog"""
    clear_screen()
    isbn = input("Enter ISBN to check out: ").zfill(3).replace(" ", "")

    # Check if the book is not found
    if isbn not in library_catalog:
        print("Book not found in the catalog.")
        time.sleep(2)

    # Check if the book is already checked out
    elif library_catalog[isbn]["available"] == False:
        print("Sorry, the book is currently checked out.")
        time.sleep(2)

    else:
        # Mark the book as checked out
        library_catalog[isbn]["available"] = False
        print(f"Book '{library_catalog[isbn]['title']}' checked out successfully.")

        # Ask if the user wants to check out another book
        another = input("Do you want to check out another book? (y/n): ").lower()
        if another == "y":
            clear_screen()
            check_out_book()
        else:
            print()


def check_in_book():
    """Function to check in a borrowed book"""
    clear_screen()
    isbn = input("Enter ISBN to check in: ").zfill(3).replace(" ", "")

    # Check if the book is not found
    if isbn not in library_catalog:
        print("Book not found in the catalog.")
        time.sleep(2)

    # Check if the book is already available
    elif library_catalog[isbn]["available"] == True:
        print("The book is actually available in the catalog.")
        time.sleep(2)

    else:
        # Mark the book as available
        library_catalog[isbn]["available"] = True
        print(f"Book '{library_catalog[isbn]['title']}' checked in successfully.")

        # Ask if the user wants to check in another book
        another = input("Do you want to check in another book? (y/n): ").lower()
        if another == "y":
            clear_screen()
            check_in_book()
        else:
            print()


def list_books():
    """Function to list all books in the catalog"""
    clear_screen()
    print("Library Catalog:")

    # Loop through all books and display their details
    for key in library_catalog.keys():
        print(
            f"ISBN: {key}, Title: {library_catalog[key]['title']}, Author: {library_catalog[key]['author']}, Available: {library_catalog[key]['available']}"
        )

    input("Press any key to go back to the main menu . . . ")
    print()


while True:
    # Main menu loop
    clear_screen()

    # Display the menu options
    print("Menu:")
    print("1. Add Book")
    print("2. Check Out Book")
    print("3. Check In Book")
    print("4. List Books")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ").strip()

    # Add a new book
    if choice == "1":
        add_book()

    # Check out a book
    elif choice == "2":
        check_out_book()

    # Check in a book
    elif choice == "3":
        check_in_book()

    # List all books
    elif choice == "4":
        list_books()

    # Exit the program
    elif choice == "5":
        print("Exiting the program . . .")
        break

    # Handle invalid choices
    else:
        print("Invalid choice. Try again")
        time.sleep(2)
