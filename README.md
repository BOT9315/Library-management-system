# 📚 Library Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-CLI%20App-orange?style=for-the-badge)

A simple and beginner-friendly **Library Management System** built with **Python**. This command-line application allows users to manage books in a library — add, view, issue, and return books with ease.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Run the App](#run-the-app)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 About the Project

This is a **command-line based Library Management System** written in Python. It is designed to simulate basic library operations without the need for any database or external library — everything runs in memory using Python dictionaries.

Perfect for beginners learning Python fundamentals like functions, dictionaries, modules, and control flow.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | ➕ **Add Book** | Add a new book with title and author to the library |
| 2 | 📖 **View Books** | Display all books currently available in the library |
| 3 | 📤 **Issue Book** | Issue an available book (removed from library for 14 days) |
| 4 | 📥 **Return Book** | Return a previously issued book back to the library |
| 5 | 🚪 **Exit** | Exit the application gracefully |

---

## 🗂 Project Structure

```
Library-management-system/
│
├── main.py          # Entry point — main menu and app loop
├── add_books.py     # Logic to add a new book
├── show_books.py    # Logic to display all available books
├── issue_books.py   # Logic to issue a book to a user
├── return_books.py  # Logic to return an issued book
├── utils.py         # Shared data stores (books, issued_books, etc.)
└── README.md
```

### 📄 File Descriptions

- **`main.py`** — Runs the main menu loop, takes user input and calls the appropriate module.
- **`utils.py`** — Stores shared dictionaries (`books`, `issued_books`) used across all modules.
- **`add_books.py`** — Prompts for book title and author, then adds it to the `books` dictionary.
- **`show_books.py`** — Iterates over the `books` dictionary and displays all available books.
- **`issue_books.py`** — Moves a book from `books` to `issued_books`, simulating a 14-day loan.
- **`return_books.py`** — Moves a book back from `issued_books` to `books`.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.x** installed on your system
- No external libraries required ✅

Check your Python version:
```bash
python --version
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/BOT9315/Library-management-system.git
   ```

2. **Navigate into the project folder**
   ```bash
   cd Library-management-system
   ```

### Run the App

```bash
python main.py
```

---

## 💻 How It Works

When you run `main.py`, you will see this menu:

```
1. Add Book in Library
2. View Books in Library
3. Issue Book from Library
4. Return Book to Library
5. Exit Library Management System

Enter your choice:
```

### Example Workflow

```
# Add a book
Enter book title: The Alchemist
Enter author name of the book: Paulo Coelho
Book 'The Alchemist' added successfully in the library!

# View books
Books in the library are present:
1. The Alchemist by Paulo Coelho

# Issue a book
Books available for issue are:
1. The Alchemist
Enter book number to issue from library: 1
Book issued! Please return it within 14 days.

# Return a book
Issued Books are:
1. The Alchemist
Enter book number to return to the library: 1
Book returned successfully!
```

> ⚠️ **Note:** All data is stored in memory. Books will reset when the program is closed.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit
   ```bash
   git commit -m "Add: your feature description"
   ```
4. Push and open a Pull Request
   ```bash
   git push origin feature/your-feature-name
   ```

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 📬 Contact

**BOT9315**  
GitHub: [@BOT9315](https://github.com/BOT9315)

---

<p align="center">Made with ❤️ using Python</p>
