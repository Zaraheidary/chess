from library_project.library import Library
from library_project.book import Book

class Launch:
    def __init__(self):
        self.library = Library()
    def add_book_from_file(self):
        file_path = "F:\\Library\\libraryfile.txt"
        try:
            with open(file_path, "r") as file:
                for line in file:
                    #each line in the file contains title,author, genre and copies that separated by ","
                    title, author, genre, copies = line.strip().split(",")
                    book = Book(title, author, genre, int(copies))
                    self.library.add_book(book) 

        except FileNotFoundError:
            print(f"The file '{file_path}' is not found")
            return False
        
    def user_input(self, answer):
        valid_inputs = "bradsg"
        return answer.lower() in valid_inputs

    def call_tasks(self, answer):
        if answer == "b" or answer == "r":
            self.borrow_return(answer)
        elif answer == "a":
            self.add_book()
        elif answer == "d":
            self.library.display_books()
        elif answer == "s":
            self.search_books()
        elif answer == "g":
            self.library.generate_report()
    
    def borrow_return(self, action):
        book_name = input("Enter the name of the book: ")
        book = self.find_book_by_title(book_name)
        if book:
            if action == "b":
                book.borrow_book()
            else:
                book.return_book()
        else:
            print("Book not found in the library.")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")
        copies = int(input("Enter the number of copies: "))
        book = Book(title, author, genre, copies)
        self.library.add_book(book)

    def search_books(self):
        search_criteria = self.get_search_criteria()
        if search_criteria:
            self.library.search_book_by_title(search_criteria[0])
            self.library.search_book_by_author(search_criteria[1])
            self.library.search_book_by_genre(search_criteria[2])

    def get_search_criteria(self):
        book_name = input("Enter the name of the book (press enter to skip): ")
        book_author = input("Enter the name of the author (press enter to skip): ")
        book_genre = input("Enter the genre of the book (press enter to skip): ")
        return book_name.strip(), book_author.strip(), book_genre.strip()

    def find_book_by_title(self, title):
        for book in self.library.books:
            if book.title.lower() == title.lower():
                return book
        return None
