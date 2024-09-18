class Book:
    """A class representing a book."""
    def __init__(self, title, author, genre, copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies
        self.available_copies = copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book borrowed successfully.")
        else:
            print("Sorry, this book is currently not available.")

    #Return a string representation of the Book object.
    def return_book(self):
        if self.available_copies < self.copies:
            self.available_copies += 1
            print("Book returned successfully.")
        else:
            print("Invalid operation. All copies are already available.")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Available Copies: {self.available_copies}"
