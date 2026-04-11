from utils import books, issued_books

def issue_books():
    if not books:
        print("No books are available for issue, sorry for your inconvenience. Please check back later.")
        return
    else:
        print("\nBooks available for issue are:")

    for book_id, book in books.items():
        print(f"{book_id}. {book['title']}")

    choice = input("Enter book number to issue from library: ").strip() 

    if choice.isdigit():
        choice = int(choice)

        if choice in books:
            issued_books[choice] = books.pop(choice)   # move book
            print("Book issued! Please return it within 14 days.")
        else:
            print("Invalid number or book already issued.")
    else:
        print("Invalid input. Please enter a valid book number.")
