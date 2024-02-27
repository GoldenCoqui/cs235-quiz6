from abc import ABC, abstractmethod

# Interfaces
class BookCatalog(ABC):
    @abstractmethod
    def search_books(self, title=None, author=None, genre=None):
        pass

class BookManagement(ABC):
    @abstractmethod
    def add_book(self, title, author, genre):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

class BookBorrowing(ABC):
    @abstractmethod
    def borrow_book(self, user_id, book_id):
        pass

    @abstractmethod
    def return_book(self, user_id, book_id):
        pass

class ReportsGenerator(ABC):
    @abstractmethod
    def generate_reports(self):
        pass

# Concrete classes implementing the interfaces
class GuestUser(BookCatalog):
    def search_books(self, title=None, author=None, genre=None):
        print("Guest user searching for books.")

class Librarian(BookManagement, BookBorrowing, ReportsGenerator):
    def add_book(self, title, author, genre):
        print("Librarian adding a book.")

    def remove_book(self, title):
        # Dummy implementation for remove_book for librarian
        print("Librarian removing a book.")

    def borrow_book(self, user_id, book_id):
        print(f"Librarian borrowing a book for user {user_id}.")

    def return_book(self, user_id, book_id):
        print(f"Librarian returning a book for user {user_id}.")

    def generate_reports(self):
        print("Librarian generating reports.")

class main():
    # Creating instances of users
    guest_user = GuestUser()
    librarian = Librarian()

    # Using methods for guest user
    guest_user.search_books()

    # Using methods for librarian
    librarian.add_book("Book1", "Author1", "Genre1")
    librarian.generate_reports()

if __name__ == "__main__":
    main()
