# Chương trình quản lý thư viện cơ bản
# update 17/9/2025
from Book import Novel, Textbook, Magazine
from Library import books,members
from Member import Member
    
#Manager-------
def AddBook():
        while True:    
                type_of_book_menu= ["1. Novel","2. Magazine","3. Textbook","4. Exit"]
                for menu in type_of_book_menu:
                        print(menu)
                try:
                        type_of_book=int ( input("Type of book: ")) 
                except Exception as e:
                       print(e)
                       continue
                match type_of_book: 
                        case 1: 
                                book_Name= input("Book Name: ")
                                book_id= input_book_id()
                                author_name= input("Auther's name: ")
                                genre= input("Genre ")
                                suitable_age=Check_suitable_age()
                                books.add_book(Novel(book_Name,author_name,book_id,genre,suitable_age,))
                                print("Book added successfully.")
                                break                               
                        case 2:
                                book_Name= input("Book Name: ")
                                book_id= input_book_id()
                                author_name= input("Auther's name: ")
                                while True:
                                        try:
                                                issue_number=int(input("Issue Number: "))
                                                if issue_number<0 :
                                                        print("Please enter positive integer!")
                                                else:
                                                        break
                                        except Exception as e:
                                                print (e)
                                while True:
                                        try:
                                                month=int(input("Month Release: "))
                                                if month<0 or month >12 :
                                                        print("Please enter month of a year!")
                                                else:
                                                        break
                                        except Exception as e:
                                                print(e)
                                books.add_book(Magazine(book_Name,author_name,book_id,issue_number,month,)) 
                                print("Book added successfully.")
                                break
                        case 3: 
                                book_Name= input("Book Name: ")
                                book_id= input_book_id()
                                author_name= input("Auther's name: ")
                                subject= input("Subject: ")
                                suitable_age=Check_suitable_age()
                                books.add_book(Textbook(book_Name,author_name,book_id,subject,suitable_age,)) 
                                print("Book added successfully.")
                                break
                        case 4: 
                                print("Exit!")
                                break
def DelBook():
        delete_book= False
        book_id= input("Enter book's id you want to delete: ")
        for book in books:
                if book.getBookId() == book_id:
                        if book.state != "Available":
                                print("Cannot delete. The book is currently borrowed.")
                                return
                        books.remove_book(book)
                        delete_book= True
                        break
        if delete_book:
                print("Delete Success!")
        else :
                print("Failed to delete!")   
def Borrow_Book():
        not_Found= True
        member_id= input("Enter member's id: ")
        book_id= input("Enter book's id : ")
        for member in members:
                if member.getMemberId() == member_id:
                        borrower= member
                        not_Found= False
                        break
        if not_Found:
               print("Not Found!")
               return
        for book in books:
                if book_id == book.getBookId():
                        if book.state == "Available":
                                book.state = "Borrowed"
                                book.borrower= borrower
                                borrower.borrowedBook.append(book)
                                print(f"{borrower.getMemberName()} borrowed {book.getBookName()} successfully!")
                                return
                        else:
                                print("Book already borrowed!")
                                return
        print("Book not found!")
def Return_Book():#camel case và snake case
        book_borrowed=None
        isMember=False
        member_id= input("Enter member's id: ")
        book_id= input("Enter book's id : ")
        for book in books:
                if book_id == book.getBookId():
                        if book.state == "Available":
                                print("Return failed. The book has not been borrowed.")
                                return
                        
                        if book.borrower.getMemberId() != member_id:
                                print("Return failed. This book was borrowed by another member.")
                                return
                        book_borrowed= book        
                        break
        if book_borrowed == None:
                print("Not found book's id!")
                return
        for member in members:
                if member.getMemberId() == member_id:
                        member.borrowedBook.remove(book_borrowed)
                        isMember= True
                        break
        if isMember:
                print(f"{member.getMemberName()} returned {book_borrowed.getBookName()} successfully!")
        else :
                print("Not found member's id!")
      
#Member Manager------------     
def register_a_new_member():
        name= input("Name: ")
        while True:
                member_id= input("Member's ID: ")
                for member in members:
                       if member.getMemberId()==member_id:
                                print("The ID already exists. Please use a unique ID.")
                                continue
                       else :   
                                members.add_member(Member(name,member_id))
                                print("Register a new member success!")
                                return
def Check_suitable_age():
    while True:
        try:
            suitable_age = int(input("Suitable age: "))
            if 0 <= suitable_age <= 150:
                return suitable_age
            else:
                print("Please enter a valid age!")
        except ValueError:
            print("Please enter a valid number!")

def checkBookId(book_id):  
        for book in books:
                if book.getBookId() == book_id:
                        return False
        return True

def input_book_id():
        while True:
                book_id = input("ID: ")
                if checkBookId(book_id):
                        return book_id
                else:
                        print("The ID already exists. Please use a unique ID.") 

     
