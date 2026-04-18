# 📚 Library Management System

A simple command-line based Library Management System built in Python that allows librarians to manage books, issue them to students, and handle returns with automatic fine calculation.

---

## 📁 Project Structure

```
library-management-system/
├── main.py           # Entry point — runs the main menu loop
├── add_books.py      # Logic for adding new books
├── show_books.py     # Logic for displaying available books
├── issue_books.py    # Logic for issuing books to students
├── return_books.py   # Logic for returning books and calculating fines
└── utils.py          # Shared data stores and fine calculation utility
```

---

## ✨ Features

- **Add Books** — Add new books to the library with title and author
- **View Books** — Display all currently available books
- **Issue Books** — Issue a book to a student for a specified number of days
- **Return Books** — Return a book and automatically calculate any overdue fine
- **Fine Calculation** — Progressive late fee system that increases week by week

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

### Run

```bash
python main.py
```

---

## 🖥️ Usage

On launch, you'll see the main menu:

```
Welcome to the Library Management System!

1. Add Book in Library
2. View Books in Library
3. Issue Book from Library
4. Return Book to Library
5. Exit Library Management System
```

Follow the on-screen prompts to perform any operation.

---

## 💸 Fine Schedule

If a book is returned late, fines are charged progressively:

| Week     | Fine per Day |
|----------|-------------|
| Week 1   | Rs. 10      |
| Week 2   | Rs. 20      |
| Week 3   | Rs. 60      |
| Week 4   | Rs. 240     |
| ...      | (continues) |

The fine multiplier increases each week, so the sooner you return the book, the better!

---

## ⚠️ Limitations

- Data is **not persisted** between sessions (stored in memory only)
- Designed for single-user, single-session use
- No authentication or user roles

---

## 🛠️ Future Improvements

- [ ] Add file/database persistence (JSON or SQLite)
- [ ] Support searching books by title or author
- [ ] Add admin and student login roles
- [ ] Generate return receipts or reports
- [ ] Build a GUI or web interface

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📬 Contact

**BOT9315**
GitHub: [@BOT9315](https://github.com/BOT9315)

---

<p align="center">Made with ❤️ using Python</p>
