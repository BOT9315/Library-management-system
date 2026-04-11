from utils import books

def show_books():
    if not books:
        print("No books in the library,sorry for your inconvenience. Please check back later.")
    else:
        print("\nBooks in the library are present:")
        for book_id, book in books.items():
            print(f"{book_id}. {book['title']} by {book['author']}")
