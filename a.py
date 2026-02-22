class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return(f"Title: {self.title}, "
               f"Author: {self.author}, "
               f"ISBN: {self.isbn},"
               f"Borrowed: {'Yes' if self.is_borrowed else 'No'}")


book1 =Book("Python crash course","Eric Mathews","1593279")
book2 =Book("Automate the boring stuff with python","AI sweigart","1593278")
book3 =Book("The pragmatic programmer","Joshua Bloch","1593374")

class User:
    def __init__(self,name,email,user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def __str__(self):
        return (f"Name: {self.name},  "
                f"Email: {self.email}, "
                f"User_ID: {self.user_id}. ")

class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
    
    def list_books(self):
        if not self.books:
            print('No book in the library.')
        for book in self.books:
            print(book)

    def borrow_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'. ")
                return
        print("Book is not available. Or has been borrowed")

    def return_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'. ")
                return
        print("Book is not available. Or has been borrowed")


    def add_users(self, user):
        if user.user_id in self.users:
            print(f"User_ID {user.user_id} already exist")
            return
        self.users[user.user_id] = user
        print(f"User '{user.name}' added with ID {user.user_id}.")
library = Library()


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()

print()

library.borrow_book("1593279")
library.borrow_book("1593278")
library.borrow_book("1593374")
library.borrow_book("1593279")
library.borrow_book("1593")


library.return_book("1593279")
library.return_book("1593278")
library.return_book("1593374")
library.return_book("1593279")
library.return_book("1593")

library.add_users(User("John Zulu","Johnzulu@outlook.com","01"))
library.add_users(User("Gilbert Mbala","Gilbert@gmail.com" "22"))
library.add_users(User("Josias Sakala","Josias@icloud.com","24"))

