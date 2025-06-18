# Library Management System

class Library:
    def __init__ (self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = int(availability)

    def BorrowBook(self, title):
        print("Borrowing..." + title + " Book.")
        if self.availability > 0:
            self.availability -= 1
            print("Successfully Borrowed!")
    def returnBook(self, title):
        print("Returned..." + title + " Book.")
        self.availability += 1
    def BookAvailable(self):
        print("Book Available...")

def is_valid_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# input part
def AddBook():
    print("\n[Enter Book Information]")
    title = input("Enter Title: ")
    author = input("Enter Author Name: ")
    availability = input("Enter Number of Availability: ")
    while not is_valid_number(availability):
        print("\nInvalid Input! Please enter a valid number.\n")
        availability = input("Enter Number of Availability: ")
    return title,author,availability


def main():
    books = []
    while True:
        print("=" * 30)
        print("{:^30}".format("Library Management System"))
        print("=" * 30)
        print("1. Add Book ")
        print("2. Borrow Book ")
        print("3. Return Book ")
        print("4. View Books ")
        print("5. Exit")

        choice = input("Enter your choice 1-5: ")

        if choice == "1":
            title, author, availability = AddBook()
            books.append(Library(title, author, availability))
            print("\nBook: "+ title + " Added Successfully!")

        elif choice == "2":
            for i, book in enumerate(books, 1):
                print(f"{i}: {book.title}")

            enteredSelection = int(input("Select Book you want to borrow: "))
            for i, book in enumerate(books, 1):
                if int(i) == enteredSelection:
                    book.BorrowBook(book.title)

        elif choice == "3":
            for i, book in enumerate(books, 1):
                print(f"{i}: {book.title}")

            enteredSelection = int(input("Select Book you want to Return: "))
            for i, book in enumerate(books, 1):
                if int(i) == enteredSelection:
                    book.returnBook(book.title)

        elif choice == "4":
            if not books:
                print("\nNo Books Available!")
            else:
                print("\n[Books in Library]\n")
                print("=" * 20)
                for book in books:
                    print(f"Book: {book.title}\nAuthor: {book.author}\nAvailability: {str(book.availability)}")
                    print("=" * 20)
        elif choice == "5":
            print("Exit Program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
