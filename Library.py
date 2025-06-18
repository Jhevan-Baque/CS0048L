class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = int(availability)

    def borrow(self):
        if self.availability > 0:
            self.availability -= 1
            print(f"\nSuccessfully borrowed '{self.title}'!")
        else:
            print(f"\nSorry, '{self.title}' is currently not available.")

    def return_book(self):
        self.availability += 1
        print(f"\nReturned '{self.title}' successfully.")

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available Copies: {self.availability}")
        print("-" * 20)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"\nBook '{book.title}' added successfully!")

    def list_books(self):
        if not self.books:
            print("\nNo books in the library yet.")
            return False
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. {book.title} by {book.author} - {book.availability} copies")
        return True

    def borrow_book(self):
        if not self.list_books():
            return
        choice = input("Enter the number of the book to borrow: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.books):
            self.books[int(choice)-1].borrow()
        else:
            print("Invalid selection.")

    def return_book(self):
        if not self.list_books():
            return
        choice = input("Enter the number of the book to return: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.books):
            self.books[int(choice)-1].return_book()
        else:
            print("Invalid selection.")

    def view_books(self):
        if not self.books:
            print("\nNo books to show.")
        else:
            print("\n[Books in Library]")
            print("=" * 20)
            for book in self.books:
                book.display()


def is_valid_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def main():
    library = Library()

    while True:
        print("\n" + "=" * 30)
        print("{:^30}".format("Library Management System"))
        print("=" * 30)
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\n[Enter Book Information]")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            availability = input("Enter Number of Copies: ")
            while not is_valid_number(availability):
                print("Invalid input! Please enter a number.")
                availability = input("Enter Number of Copies: ")
            new_book = Book(title, author, availability)
            library.add_book(new_book)

        elif choice == "2":
            library.borrow_book()

        elif choice == "3":
            library.return_book()

        elif choice == "4":
            library.view_books()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()