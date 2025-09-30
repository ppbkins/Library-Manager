from Book import Novel, Magazine, Textbook
from Member import Member
class Book_List:
        def __init__(self):
                self.books=[]
        def __iter__(self):      
                return iter(self.books)
        def add_book(self,book):
                self.books.append(book)
        def remove_book(self,book):
                self.books.remove(book)
        def show_books(self):
                print("\n")
                print("====Novel==== ")
                print("\n")
                print(Novel.title())
                for book in self.books:
                        if isinstance(book,Novel):
                                print(book.data())
                                print_Borrower_List(book)
                                print("-"*50) 
                print("\n")
                print("====Magazine====")
                print("\n")
                print(Magazine.title())
                for book in self.books:
                        if isinstance(book,Magazine):
                                print(book.data())
                                print_Borrower_List(book)
                                print("-"*50) 
                print("\n")
                print("====Textbook====")
                print("\n")
                print(Textbook.title())
                for book in self.books:
                        if isinstance(book,Textbook):
                                print(book.data())
                                print_Borrower_List(book)
                                print("-"*50)              
class Member_List:
        def __init__(self):
                self.members=[]
        def add_member(self,member):
                self.members.append(member)
        def __iter__(self):
               return iter(self.members)
        def del_member(self,member_id):
                for member in self.members:
                        if member.getMemberId()== member_id:
                                self.members.remove(member)
        def show_members(self):
                print(Member.title())
                for member in self.members:
                        print(member.data())
books= Book_List()
members=Member_List()
def print_Borrower_List(book):
    if book.borrower is None:
        print("Borrower's Name: None")
    else:
        print(f"Borrower's Name: {book.borrower.getMemberName()}")  