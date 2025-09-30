from Book import Magazine, Novel, Textbook
from Member import Member
from Library import books, members
import random
#Fake date----------------
sample_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ian", "Jack"]
sample_books = ["BookA", "BookB", "BookC", "BookD", "BookE", "BookF", "BookG", "BookH", "BookI", "BookJ"]
sample_authors = ["Author1", "Author2", "Author3", "Author4", "Author5"]
def generate_sample_data():
    # Generate 10 Novels
    for i in range(10):
        book = Novel(
            Book_Name=random.choice(sample_books) + f"_N{i+1}",
            Author_Name=random.choice(sample_authors),
            book_id=f"N{i+1:03d}",
            genre=random.choice(["Romance", "Horror", "Adventure", "Fantasy"]),
            suitable_age=random.randint(12, 60)
        )
        books.add_book(book)

    # Generate 10 Magazines
    for i in range(10):
        book = Magazine(
            Book_Name=random.choice(sample_books) + f"_M{i+1}",
            Author_Name=random.choice(sample_authors),
            book_id=f"M{i+1:03d}",
            Issue_Number=random.randint(1, 100),
            Month=random.randint(1, 12)
        )
        books.add_book(book)

    # Generate 10 Textbooks
    for i in range(10):
        book = Textbook(
            Book_Name=random.choice(sample_books) + f"_T{i+1}",
            Author_Name=random.choice(sample_authors),
            book_id=f"T{i+1:03d}",
            subject=random.choice(["Math", "Physics", "History", "Biology", "Literature"]),
            suitable_age=random.randint(6, 25)
        )
        books.add_book(book)

    # Generate 10 Members
    for i in range(10):
        member = Member(
            name=random.choice(sample_names),
            member_id=f"M{i+1:03d}"
        )
        members.add_member(member)
