from utils import books, issued_books, calculate_fine
from datetime import datetime

def return_books():
    if not issued_books:
        print("No issued books to return to the library.")
        return

    print("\nIssued Books are:")
    for book_id, book in issued_books.items():
        print(f"{book_id}. {book['title']} (issued to {book['student_name']}, due in {book['days_allotted']} days from {book['issue_date']})")

    choice = input("Enter book number to return to the library: ")
    
    if choice.isdigit():
        choice = int(choice)
        if choice in issued_books:
            issue_date = datetime.strptime(issued_books[choice]["issue_date"], "%Y-%m-%d").date() #data of submission
            today = datetime.today().date()
            days_used = (today - issue_date).days
            days_allotted = issued_books[choice]["days_allotted"]
            days_late = days_used - days_allotted

            books[choice] = issued_books.pop(choice)   # move back

            if days_late > 0:
                fine = calculate_fine(days_late)
                print(f"Book returned {days_late} day(s) late. Fine charged: Rs.{fine}")
            else:
                print("Book returned successfully, thank you! Hope you enjoyed reading it.")
        else:
            print("Invalid number or book not issued.")
    else:
        print("Invalid input. Please enter a valid book number.")
