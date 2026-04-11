from utils import books, issued_books

def return_books():
    if not issued_books:
        print("No issued books to return to the library.")
        return

    print("\nIssued Books are:")
    for book_id, book in issued_books.items():
        print(f"{book_id}. {book['title']}")

    choice = input("Enter book number to return to the library: ")

    if choice.isdigit():
        choice = int(choice)

        if choice in issued_books:
            books[choice] = issued_books.pop(choice)   # move back
            print("Book returned successfully!")
        else:
            print("Invalid number or book not issued.")