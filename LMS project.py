
# Library Management System (Librarian Side)

LIBRARIAN_USERNAME = "librarian"
LIBRARIAN_PASSWORD = "admin123"


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False
        self.issued_to = None  # name of the member who has the book

    def display(self):
        status = "Issued" if self.issued else "Available"

        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)
        if self.issued:
            print("Issued to:", self.issued_to)


class Library:
    def __init__(self):
        self.books = []

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id.lower() == book_id.lower():
                return book
        return None

    def add_book(self):
        book_id = input("Enter Book ID: ").strip()

        if not book_id:
            print("Book ID cannot be empty.")
            return

        # Prevent duplicate Book IDs
        if self.find_book(book_id):
            print("A book with this ID already exists in the catalogue.")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        # Prevent empty book details
        if not title or not author:
            print("Title and author cannot be empty.")
            return

        self.books.append(Book(book_id, title, author))
        print("Book added to the catalogue successfully.")

    def display_books(self):
        if len(self.books) == 0:
            print("The catalogue is empty.")
        else:
            print("\n====== Library Catalogue ======")
            for book in self.books:
                book.display()
                print("-" * 25)

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ").strip()
        book = self.find_book(book_id)

        if book is None:
            print("Book not found in the catalogue.")
        elif book.issued:
            print("This book is already issued to", book.issued_to + ".")
        else:
            member_name = input("Enter member name: ").strip()
            if not member_name:
                print("Member name cannot be empty.")
                return
            book.issued = True
            book.issued_to = member_name
            print("Book issued to", member_name, "successfully.")

    def receive_returned_book(self):
        book_id = input("Enter Book ID being returned: ").strip()
        book = self.find_book(book_id)

        if book is None:
            print("Book not found in the catalogue.")
        elif not book.issued:
            print("This book was not issued.")
        else:
            print("Book received from", book.issued_to + ".")
            book.issued = False
            book.issued_to = None

    def search_book(self):
        if not self.books:
            print("The catalogue is empty.")
            return

        search_term = input("Enter Book ID or title to search: ").strip().lower()

        if not search_term:
            print("Please enter a Book ID or title.")
            return

        found_books = []

        for book in self.books:
            if (search_term == book.book_id.lower()
                    or search_term in book.title.lower()):
                found_books.append(book)

        if found_books:
            print("\n====== Search Results ======")
            for book in found_books:
                book.display()
                print("-" * 25)
        else:
            print("No matching book found.")

    def show_issued_books(self):
        issued = [book for book in self.books if book.issued]

        if not issued:
            print("No books are currently issued.")
        else:
            print("\n====== Currently Issued Books ======")
            for book in issued:
                print(book.book_id, "-", book.title, "(issued to", book.issued_to + ")")

    def show_statistics(self):
        total_books = len(self.books)
        issued_books = 0

        for book in self.books:
            if book.issued:
                issued_books += 1

        available_books = total_books - issued_books

        print("\n====== Library Report ======")
        print("Total books:", total_books)
        print("Available books:", available_books)
        print("Issued books:", issued_books)


def librarian_login():
    print("====== Librarian Login ======")
    for attempt in range(3):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username == LIBRARIAN_USERNAME and password == LIBRARIAN_PASSWORD:
            print("Login successful. Welcome, Librarian!")
            return True
        print("Incorrect username or password.")
    print("Too many failed attempts.")
    return False


def main():
    if not librarian_login():
        return

    library = Library()

    while True:
        print("""
====== Librarian Dashboard ======
1. Add New Book to Catalogue
2. View All Books
3. Issue Book to Member
4. Receive Returned Book
5. Search Catalogue
6. View Issued Books
7. Library Report
8. Logout
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            library.issue_book()
        elif choice == "4":
            library.receive_returned_book()
        elif choice == "5":
            library.search_book()
        elif choice == "6":
            library.show_issued_books()
        elif choice == "7":
            library.show_statistics()
        elif choice == "8":
            print("Logged out. Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
















































