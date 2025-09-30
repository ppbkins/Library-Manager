from Library import books, members
import Fake_Data
import Library_Manager

lm=Library_Manager

# Main---------------
def Main():
        Fake_Data.generate_sample_data()   
        while True:
                print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
                print("1. Add Book")
                print("2. Delete Book")
                print("3. Show Book List")
                print("4. Register a new Member")
                print("5. Show Member List")
                print("6. Borrow Book")
                print("7. Return Book")
                print("0. Exit")
        
                try:
                        choice = int(input("Enter your choice: "))
                except ValueError:
                        print("Invalid input! Please enter a number.")
                        continue

                if choice == 1:
                        lm.AddBook()
                elif choice == 2:
                        lm.DelBook()
                elif choice == 3:
                        books.show_books()
                elif choice == 4:
                        lm.Register_a_new_member()
                elif choice == 5:
                        members.show_members()
                elif choice == 6:
                        lm.Borrow_Book()
                elif choice == 7: 
                        lm.Return_Book()
                elif choice == 0:
                        print("Exiting program... Goodbye!")
                        break
                else:
                        print("Invalid choice! Please try again.")
if __name__== "__main__":
        Main()