from utils import books, issued_books
from datetime import datetime

def issue_books():
    if not books:
        print("No books are available for issue,sorry for your inconvenience. Please check back later.")
        return
    else:
        print("\nBooks available for issue are:")

    for book_id, book in books.items():
        print(f"{book_id}. {book['title']}")

    choice = input("Enter book number to issue from library: ").title()

    if choice.isdigit():
        choice = int(choice)

        if choice in books:
            student_name = input("Enter student name: ").title()
            days_allotted = input("Enter number of days to issue the book for: ")

            if not days_allotted.isdigit() or int(days_allotted) <= 0:
                print("Invalid number of days. Book not issued.")
                return

            days_allotted = int(days_allotted)
            issue_date = datetime.today().strftime("%Y-%m-%d")

            issued_books[choice] = books.pop(choice)   # move book
            issued_books[choice]["student_name"] = student_name
            issued_books[choice]["issue_date"] = issue_date
            issued_books[choice]["days_allotted"] = days_allotted

            print(f"Book issued to {student_name} on {issue_date}! Please return it within {days_allotted} days.")
            print("\nFine Schedule (if returned late):")
            print("  Week 1 : Rs.10 per day")
            print("  Week 2 : Rs.20 per day")
            print("  Week 3 : Rs.60 per day")
            print("  Week 4 : Rs.240 per day  (and so on...)")
        else:
            print("Invalid number or book already issued.")
        
    else:
        print("Invalid input. Please enter a valid book number.")
