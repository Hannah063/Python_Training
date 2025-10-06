class Book:
    _id = 1
    def __init__(self, book_name, author, language, genres, quantity, publication_date):
        self._book_id = Book._id
        Book._id += 1
        self._book_name = book_name
        self._author = author
        self._language = language
        self._genres = genres
        self._quantity = quantity
        self._publication_date = publication_date

    # Setter and Getter
    @property
    def book_id(self):
        return self._book_id

    @property
    def book_name(self):
        return self._book_name
    
    @book_name.setter
    def book_name(self, new_book_name):
        self._book_name = new_book_name
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self, new_language):
        self._language = new_language

    @property
    def genres(self):
        return self._genres
    
    @genres.setter
    def genres(self, new_genres):
        self._genres = new_genres

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity = new_quantity

    @property
    def publication_date(self):
        return self._publication_date
    
    @publication_date.setter
    def publication_date(self, new_publication_date):
        self._publication_date = new_publication_date