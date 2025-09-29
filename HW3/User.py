class User:
    def __init__(self, identity_card, full_name, date_of_birth, gender):
        self._identity_card = identity_card
        self._full_name = full_name
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._borrowed_books = []

    # Getter and Setter
    @property
    def identity_card(self):
        return self._identity_card

    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def borrowed_books(self):
        return self._borrowed_books
    
    @borrowed_books.setter
    def borrowed_books(self, value):
        self._borrowed_books = value