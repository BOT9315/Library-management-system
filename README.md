# 📚 Library Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-CLI%20App-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A simple and beginner-friendly **Library Management System** built with **Python**. This command-line application lets users add, view, issue, and return books — all from the terminal with zero setup required.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Example Workflow](#example-workflow)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 About the Project

The **Library Management System (LMS)** is a Python CLI project that simulates real-world library operations. No database or external libraries are required — all data is managed in memory using Python dictionaries.

It is ideal for beginners who want to practise Python concepts such as:
- Functions and modules
- Dictionaries and data manipulation
- Loops and conditional logic
- User input handling and validation

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | ➕ **Add Book** | Add a new book with title and author name |
| 2 | 📖 **View Books** | Display all books currently available in the library |
| 3 | 📤 **Issue Book** | Issue an available book — must be returned within **14 days** |
| 4 | 📥 **Return Book** | Return a previously issued book back to the library |
| 5 | 🚪 **Exit** | Exit the application gracefully |

### 🔤 Smart Input Formatting
User input is automatically converted to **Title Case** — no matter how the user types:

```
the alchemist      →   The Alchemist    ✅
PAULO COELHO       →   Paulo Coelho     ✅
tHe GrEaT gAtSbY  →   The Great Gatsby ✅
```

---

## 🗂 Project Structure

```
Library-management-system/
│
├── main.py          # Entry point — main menu loop
├── add_books.py     # Logic to add a new book
├── show_books.py    # Logic to display all available books
├── issue_books.py   # Logic to issue a book to a user
├── return_books.py  # Logic to return an issued book
├── utils.py         # Shared data stores (books, issued_books, etc.)
└── README.md
```

### 📄 File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Runs the `while True` menu loop and routes user input to the correct module |
| `utils.py` | Defines shared data: `books {}`, `issued_books {}`, `returned_books {}`, `next_id` |
| `add_books.py` | Takes title and author input, converts to Title Case, saves to `books` dict |
| `show_books.py` | Iterates over `books` and prints each book's ID, title, and author |
| `issue_books.py` | Lists available books, moves selected book from `books` → `issued_books` |
| `return_books.py` | Lists issued books, moves selected book from `issued_books` → `books` |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed on your machine
- No external packages needed ✅

Check your Python version:
```bash
python --version
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/BOT9315/Library-management-system.git
   ```

2. **Go into the project folder**
   ```bash
   cd Library-management-system
   ```

3. **Run the app**
   ```bash
   python main.py
   ```

---

## 💻 How It Works

When you run `main.py`, you will see this menu in a loop:

```
Welcome to the Library Management System!

1. Add Book in Library
2. View Books in Library
3. Issue Book from Library
4. Return Book to Library
5. Exit Library Management System

Enter your choice:
```

The menu keeps repeating until the user selects **5 to Exit**.

---

## 🔄 Example Workflow

```
# ➕ Add a book
Enter book title: the alchemist
Enter author name of the book: paulo coelho
Book 'The Alchemist' added successfully in the library!

# 📖 View books
Books in the library are present:
1. The Alchemist by Paulo Coelho

# 📤 Issue a book
Books available for issue are:
1. The Alchemist
Enter book number to issue from library: 1
Book issued! Please return it within 14 days.

# 📥 Return a book
Issued Books are:
1. The Alchemist
Enter book number to return to the library: 1
Book returned successfully, thank you! Hope you enjoyed reading it.

# 🚪 Exit
Exiting the library management system.
```

> ⚠️ **Note:** Data is stored in memory only. All records reset when the program is closed.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** this repository
2. **Create** a new branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add: your feature description"
   ```
4. **Push** your branch
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a **Pull Request** 🚀

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 📬 Contact

**BOT9315**
GitHub: [@BOT9315](https://github.com/BOT9315)

---

<p align="center">Made with ❤️ using Python</p>
