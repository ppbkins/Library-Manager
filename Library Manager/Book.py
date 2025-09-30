class Book:
        def __init__(self, Book_Name, Author_Name , book_id, state="Available",borrower=None):
                 self._Book_Name= Book_Name
                 self._Author_Name= Author_Name
                 self._book_id= book_id
                 self.state=state
                 self.borrower= borrower
        def data(self):
                return f"{self._Book_Name:<20}{self._Author_Name:<10}{self._book_id:<10}{self.state:<20}"

        def getBookId(self):
                return self._book_id
        def getBookName(self):
                return self._Book_Name
        @staticmethod
        def title():
                return f"{'Book Name':<20}{'Author\'s Name':<10}{'ID':<10}{'State':<17}"
class Textbook(Book):
        def __init__(self, Book_Name, Author_Name, book_id, subject, suitable_age,state= "Available",borrower=None):
                super().__init__(Book_Name, Author_Name, book_id,state,borrower)
                self._subject= subject
                self._suitable_age= suitable_age
        def data(self):
                return super().data()+ f"{self._subject:<15}{self._suitable_age:<10}"
        @staticmethod
        def title():
                return Book.title() +f"{'Subject':<15}{'Suitable Age':<10}"
class Novel(Book):
        def __init__(self, Book_Name, Author_Name, book_id, genre, suitable_age, state= "Available",borrower=None):
                super().__init__(Book_Name, Author_Name, book_id, state,borrower)
                self._genre= genre
                self._suitable_age= suitable_age
        def data(self):
                return super().data()+ f"{self._genre:<15}{self._suitable_age:<10}"
        @staticmethod
        def title():
                return Book.title() +f"{'Genre':<15}{'Suitable Age':<10}"
class Magazine(Book):
        def __init__(self, Book_Name, Author_Name, book_id, Issue_Number, Month, state= "Available",borrower=None):
                super().__init__(Book_Name, Author_Name, book_id, state,borrower)
                self._Issue_Number= Issue_Number
                self._Month= Month
        def data(self):
                return super().data()+ f"{self._Issue_Number:<15}{self._Month:<10}"
        @staticmethod
        def title():
                return Book.title() +f"{'Issue Number':<15}{'Month':<10}"
Books= []