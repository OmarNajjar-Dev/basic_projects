import os
import time


def clear_screen():
    os.system("cls")


books = {}


def Add():
    clear_screen()
    book_ISBN = input("Enter ISBN: ").replace(" ", "")
    book_ISBN = book_ISBN.zfill(3)

    # The ISBN must be a number
    if not book_ISBN.isdigit():
        print("That is not a number.")
        time.sleep(2)
        print()

    # The ISBN of the added book must be different from the others
    elif book_ISBN in books:
        print("This book is already in the catalog.")
        time.sleep(2)

    else:
        book_title = input("Enter title: ").strip()
        book_author = input("Enter author: ").strip()
        books[book_ISBN] = [book_title, book_author, True]
        print(
            f"Book '{books [book_ISBN] [0]}' by {books [book_ISBN] [1]} added to the catalog with ISBN {book_ISBN}."
        )

        another = input("Do you want to add another book? (y/n): ").lower()
        if another == "y":
            clear_screen()
            Add()


def Check_Out():
    clear_screen()
    check_out = input("Enter ISBN to check out: ").replace(" ", "")
    check_out = check_out.zfill(3)

    # If the book not found in the catalog
    if check_out not in books:
        print("Book not found in the catalog.")
        time.sleep(2)

    # If it has already been checked out
    elif books[check_out][2] == False:
        print("Sorry, the book is currently checked out.")
        time.sleep(2)

    # If the book is available in the category
    else:
        books[check_out][2] = False
        print(f"Book '{books [check_out] [0]}' checked out successfully.")

        another = input("Do you want to check out another book? (y/n): ").lower()
        if another == "y":
            clear_screen()
            Check_Out()
        else:
            print()


def Check_In():
    clear_screen()
    check_in = input("Enter ISBN to check in: ").replace(" ", "")
    check_in = check_in.zfill(3)

    # If the book not found in the catalog
    if check_in not in books:
        print("Book not found in the catalog.")
        time.sleep(2)

    # If the book is actually available in the catalog or has been returned
    elif books[check_in][2] == True:
        print("The book is actually available in the catalog.")

    # To retrieve the book that has been checked out from the catalog
    else:
        books[check_in][2] = False
        print(f"Book '{books [check_in] [0]}' checked in successfully.")

        another = input("Do you want to check in another book? (y/n): ").lower()
        if another == "y":
            clear_screen()
            Check_In()
        else:
            print()


def list_books():
    clear_screen()
    print("Library Catalog:")

    # To obtain the ISBN of each book in the "key"
    for key in books.keys():
        list_books = f"ISBN: {key}, Title: {books [key] [0]}, Author: {books [key] [1]}, Available: {books [key] [2]}"
        print(list_books)

    input("Press any key to go back to the main menu . . . ")
    print()


while True:
    clear_screen()

    # Main Menu
    print("Menu:")
    print("1. Add Book")
    print("2. Check Out Book")
    print("3. Check In Book")
    print("4. List Books")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ").strip()

    # Add Book
    if choice == "1":
        Add()

    # Check Out Book
    elif choice == "2":
        Check_Out()

    # Check In Book
    elif choice == "3":
        Check_In()

    # List Books
    elif choice == "4":
        list_books()

    # Exit
    elif choice == "5":
        print("Exiting the program . . .")
        break

    # Invalid
    else:
        print("Invalid choice. Try again")
        input("Press any key to continue . . .")
        print()
