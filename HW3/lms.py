from Book import Book
from User import User

class LibraryManageSystem:
    def __init__(self):
        self.__users = []
        self.__books = []

    # Book - Add
    def add_book(self, book_name, author, language, genres, quantity, publication_date):
        book = Book(book_name, author, language, genres, quantity, publication_date)
        self.__books.append(book)
        print(f"Add {book.book_name} to library")
        return book

    # Book - Update
    def update_book(self, book_id, attribute, value):
        book = self.search_book_by_id(book_id)
        if book and hasattr(book, attribute):
            setattr(book, attribute, value)
        else:
            print("Invalid attribute or id")

    # Book - Search
    def search_book_by_name(self, book_name):
        return list(filter(lambda b: book_name.upper() in b.book_name.upper(), self.__books))
    
    def search_book_by_id(self, book_id):
        return next((b for b in self.__books if b.book_id == book_id), None)

    # Book - Delete
    def delete_book(self, book_id):
        length = len(self.__books)
        self.__books = list(filter(lambda b: b.book_id != book_id, self.__books))
        if len(self.__books) < length:
            print("Delete successfully!")
        else:
            print("This book isn't existing!")

    # Books - View
    def view_books(self):
        for book in self.__books:
            print(f"{book.book_id} -- {book.book_name} -- {book.author} -- {book.language} -- {book.genres} -- {book.quantity} -- {book.publication_date}")    

    # User - Add
    def add_user(self, identity_card, full_name, date_of_birth, gender):
        user = User(identity_card, full_name, date_of_birth, gender)
        self.__users.append(user)
        print(f"Add {user.full_name} to library")
        return user

    # User - Update
    def update_user(self, identity_card, attribute, value):
        user = self.search_user_by_identity_card(identity_card)
        if user and hasattr(user, attribute):
            setattr(user, attribute, value)
        else:
            print("Invalid attribute or identity_card")

    # User - Search
    def search_user_by_name(self, user_name):
        users = list(filter(lambda b: user_name.upper() in b.full_name.upper(), self.__users))
        for user in users:
            print(f"{user.identity_card} -- {user.full_name} -- {user.date_of_birth} -- {user.gender} -- {user.borrowed_books}")
    
    def search_user_by_identity_card(self, user_identity_card):
        return next((b for b in self.__users if b.identity_card == user_identity_card), None)
    
    # User - Delete
    def delete_user(self, user_identity_card):
        length = len(self.__users)
        self.__users = list(filter(lambda b: b.identity_card != user_identity_card, self.__users))
        if len(self.__users) < length:
            print("Delete successfully!")
        else:
            print("This user isn't existing!")

    # Users - View
    def view_users(self):
        for user in self.__users:
            print(f"{user.identity_card} -- {user.full_name} -- {user.date_of_birth} -- {user.gender} -- {user.borrowed_books}")
    
    # Borrowing
    def borrow_books(self, user_identity_card, book_id, quantity):
        user = self.search_user_by_identity_card(user_identity_card)
        book = self.search_book_by_id(book_id)

        if not user or not book:
            print("User or Book not found in the system!")
            return

        if book.quantity < quantity:
            print("Requested quantity is out of stock!")
            return

        borrowed_books = user.borrowed_books
        record = next((item for item in borrowed_books if item[0] == book_id), None)

        if record:
            record[1] += quantity
        else:
            borrowed_books.append([book.book_id, quantity])

        user.borrowed_books = borrowed_books
        book.quantity -= quantity

        print(f"{book.book_name} has been borrowed by {user.full_name}!")


    # Returning
    def return_books(self, user_identity_card, book_id, quantity):
        user = self.search_user_by_identity_card(user_identity_card)

        if not user:
            print("User not found in the system!")
            return

        borrowed_books = user.borrowed_books
        record = next((item for item in borrowed_books if item[0] == book_id), None)

        if not record:
            print("You have not borrowed this book!")
            return

        record_quantity = record[1]
        if quantity > record_quantity:
            print("You can only return up to the number of books you borrowed!")
            return

        book = self.search_book_by_id(book_id)
        if book:
            book.quantity += quantity

        if quantity == record_quantity:
            borrowed_books = list(filter(lambda b: b[0] != record[0], borrowed_books))
        else:
            record[1] -= quantity

        user.borrowed_books = borrowed_books
        print(f"Returned {quantity} book(s) with ID {book_id}!")
