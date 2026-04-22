def library():
     
     while True:
        print("\nWelcome to the Library Management System!")
        print("\n1. Add Book in Library")
        print("\n2. View Books in Library")
        print("\n3. Issue Book from Library")
        print("\n4. Return Book to Library")
        print("\n5. Exit Library Management System")

        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice=int(choice)
            if choice == 1:
                from add_books import add_books
                add_books()
            elif choice == 2:
                from show_books import show_books
                show_books()
            elif choice == 3:
                from issue_books import issue_books
                issue_books()
            elif choice == 4:
                from return_books import return_books
                return_books()
            elif choice == 5:
                print("Exiting the library management system.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number corresponding to the options. THANK YOU!")
library()
