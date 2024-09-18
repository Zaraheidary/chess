class Library:
    """    A class representing a library.    """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added to the library.")

    def display_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

    def search_book_by_title(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
            
        if found_books:
            print("Books found with title '{}':".format(title))
            for book in found_books:
                print(book)
        else:
            print("No books found with title '{}'.".format(title))

    def search_book_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        if found_books:
            print("Books found with author '{}':".format(author))
            for book in found_books:
                print(book)
        else:
            print("No books found with author '{}'.".format(author))

    def search_book_by_genre(self, genre):
        found_books = []
        for book in self.books:
            if book.genre.lower() == genre.lower():
                found_books.append(book)
        if found_books:
            print("Books found with genre '{}':".format(genre))
            for book in found_books:
                print(book)
        else:
            print("No books found with genre '{}'.".format(genre))

    def generate_report(self):
        total_books = len(self.books)
        total_available_copies = sum(book.available_copies for book in self.books)
        print("Library Report:")
        print("Total Books: {}".format(total_books))
        print("Total Available Copies: {}".format(total_available_copies))
