class Book:
    def __init__(self, book_id, title, author, year):
        
        try:
            book_id= int(input("Book ID: "))
        except ValueError:
            print("Book ID must be an integer.")
        self.id=book_id    
        self.title=title
        self.author=author
        self.year=year
        self.available=True
        if self.available is False:
                raise ValueError("This book is already borrowed.")
    def display_info(self):
        status="Available" if self.available else "Not available"
        print(f"ID: {self.id}")  
        print(f"Title: {self.title}")  
        print(f"Author: {self.author}")  
        print(f"Year: {self.year}")  
        print(f"Status: {status}")
    def borrow(self):
        self.available=False
    def return_book(self):
        self.available=True
        
class Member:
    def __init__(self, member_id, name, email):
        self.id=member_id
        self.name=name
        self.author=email
        self.borrowed_books=[]
    def display_info(self):
        status="Available" if self.available else "Not available"
        print(f"ID: {self.id}")  
        print(f"Name: {self.name}")  
        print(f"Email: {self.email}")  
        print(f"Books Reading: {self.borrowed_books}") 
    def borrow_book(self, book):
        book.borrow()
        self.borrowed_books.append(book)
        
    def return_book(self, book):
        index=0
        for book_bor in self.borrowed_books:
            if(book.id == book_bor.id):
                break
            index += 1
            
        self.borrowed_books.remove(index)
        book.return_book()
class Library :  
    def __init__(self):
        self.books=[]
        self.members=[]  
    def add_book(self,book):
        self.books.append(book)
    def add_member(self,member):
        self.books.append(member)
    def find_book(self,book_id):
        for book in self.books:
            if(book.id == book_id):
                return book
        return None    
    def find_member(self,member_id):
        for member in self.members:
            if(member.id == member_id):
                return member
        return None
    def borrow_book(self,member_id, book_id):
        book= self.find_book(self, book_id)
        member= self.find_member(self, member_id)
        member.borrow_book(book)
    def return_book(self,member_id,book_id):
        book= self.find_book(self, book_id)
        member= self.find_member(self, member_id)
        member.return_book(book)
    def display_books(self):
        for book in self.books:
            print(book) 
    def display_members(self):
        for member in self.members:
            print(member)                  
                  
class PhysicalBook(Book):
    def __init__(self,book_id, title, author, year, shelf_number):
        super().__init__(book_id, title, author, year)
        self.shelf_number=shelf_number
    def display_info(self):
        status="Available" if self.available else "Not available"
        print(f"ID: {self.id}")  
        print(f"Title: {self.title}")  
        print(f"Author: {self.author}")  
        print(f"Year: {self.year}")  
        print(f"Status: {status}")
        print(f"Shelf Number: {self.shelf_number}")
class EBook(Book):
    def __init__(self,book_id, title, author, year, file_size, format):
        super().__init__(book_id, title, author, year)
        self.file_size= file_size
        self.format=format 
    def display_info(self):
        status="Available" if self.available else "Not available"
        print(f"ID: {self.id}")  
        print(f"Title: {self.title}")  
        print(f"Author: {self.author}")  
        print(f"Year: {self.year}")  
        print(f"Status: {status}") 
        print(f"File Size: {self.file_size}")
        print(f"Format: .{self.format}")         

book1=Book(1,"Clean Code", "Robert C.Martin", 2008)   
book2=Book(2,"Python Crash Course", "Eric Matthes", 2023)  
member1=Member(1, "Ismail","ismail33@gmail.com")  
member2=Member(2, "Ahmed","ahmad33@gmail.com")  

book1.display_info()
member1.display_info()
        