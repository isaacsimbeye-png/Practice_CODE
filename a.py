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
    def __init__(self,user_id,name,email):
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
    
    def list_users(self):
        if not self.users:
            print("No users registered")
            return
        for user_id,user in self.users.items():
            print(user)

    def update_user(self,user_id, name =None, email =None):
        if user_id not in self.users:
            print("User not found")
            return
        if name:
            self.users[user_id].name = name
        if email:
            self.users[user_id].email = email
        print(f"User '{user_id}' updated. ")

    def delete_user(self,user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User {user_id} deleted. ")
        else:
            print("User not found. ")

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

print()

library.return_book("1593279")
library.return_book("1593278")
library.return_book("1593374")
library.return_book("1593279")
library.return_book("1593")

print()

library.add_users(User("11", "John Chinena","John@outlook.com"))
library.add_users(User("12","Thee Developer","Gilbert@gmail.com"))
library.add_users(User("13","Big bro","Josias@icloud.com"))

print()

library.update_user("11",name="Jacob", email ="update@example.com")
library.update_user("12",email="Eagleone@gmail.com")


print()
library.list_users()

print()
library.delete_user("13")
library.delete_user("13")

print()
library.list_users()

