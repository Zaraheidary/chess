from library_project.library import Library
from library_project.book import Book
from library_project.launch import Launch
#from IPython import clear_output

launch = Launch()
launch.add_book_from_file()
print("Welcome to Library management")
while True:
    task = input("What do you want to do? (borrow(b) or return(r) a book, add(a) a book, display(d) available books, search(s) for books, general(g) report of books) please enter one of these tasks: ")
    if launch.user_input(task):
        launch.call_tasks(task[0].lower())
        another_task = input("do you want to do another task?(y/n)")
        if another_task[0].lower() == "y":
            pass
            #clear_output()
        else:
            break
    else:
        print("Please enter a correct task!")
        #clear_output()
