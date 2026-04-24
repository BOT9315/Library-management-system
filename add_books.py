from utils import books, next_id
def add_books():
    global next_id

    title = input("Enter book title: ").title()
    author = input("Enter author name of the book: ").title()

    books[next_id] = {"title": title,"author": author}

    print(f"Book '{title}' added successfully in the library!")

    next_id += 1
