from User import User
from Book import Book
from lms import LibraryManageSystem

if __name__ == "__main__":
    library = LibraryManageSystem()

    user_1 = library.add_user("123456789", "Ho Thi Thanh Huyen", "09-09-2004", "female")
    user_2 = library.add_user("123456780", "Tran Phi Vu", "08-09-2004", "male")

    book_1 = library.add_book("Sans famille", "Hector Malot", "French", "Classics, Fiction, Childrens, France, Novels", 6, "07-05-2002", )
    book_2 = library.add_book("Les Miserables", "Victor Hugo", "English", "Fiction General", 10, "21-02-2017")

    library.borrow_books(user_1.identity_card, book_1.book_id, 7)
    library.borrow_books(user_2.identity_card, book_2.book_id, 5)
    library.borrow_books(user_1.identity_card, book_1.book_id, 3)
    library.borrow_books(user_2.identity_card, book_1.book_id, 3)

    print("==========================Books==============================")
    library.view_books()

    print("==========================Users==============================")
    library.view_users()

    library.update_user(user_1.identity_card, "full_name", "Ho Thi Huyen")

    print("==========================Users==============================")
    library.view_users()

    print("==========================Search User==============================")
    print(library.search_user_by_name("huYen"))

    library.return_books(user_2.identity_card, book_2.book_id, 6)
    library.return_books(user_2.identity_card, book_2.book_id, 5)
    library.return_books(user_1.identity_card, book_1.book_id, 3)
    library.return_books(user_2.identity_card, book_1.book_id, 1)

    print("==========================Users==============================")
    library.view_users()

    print("==========================Books==============================")
    library.view_books()
