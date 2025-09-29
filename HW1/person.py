import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.__name = name
        self.__country = country
        self.__date_of_birth = date_of_birth

    @property
    def name(self):
        return self.__name
    
    @property
    def date_of_birth(self):
        return self.__date_of_birth

    def calculate_age(self):
        now = datetime.datetime.now()
        if now.month < self.date_of_birth.month:
            return now.year - self.date_of_birth.year - 1
        else:
            return now.year - self.date_of_birth.year
    
person_1 = Person("Ho Thi Huyen", "Vietnam", datetime.datetime(2004, 10, 9))
person_2 = Person("Tran Phi Vu", "China", datetime.datetime(2000, 8, 9))

print(f"Age of {person_1.name}: {person_1.calculate_age()} years old!")
print(f"Age of {person_2.name}: {person_2.calculate_age()} years old!")