# importing sqlite3
import sqlite3
db = sqlite3.connect('ebookstore_db')


# Creating function called create_db for creating new database
def create_db():

    # Getting a cursor
    cursor = db.cursor()
    #  Creating a table called books
    cursor.execute('''CREATE TABLE if not exists books(Id INTEGER PRIMARY KEY not null,
        title varchar(255) not null, 
        author TEXT(100),
        qty INTEGER not null)''')
    db.commit()

# inserting initial books data into database
    initial_books = [(3001,'A Tale of Two Cities','Charles Dickens',30),
                     (3002,'Harry Potter and the Philosophers Stone','J.K. Rowling',40),
                     (3003,'The Lion, the Witch and the Wardrobe','C. S. Lewis',25),
                     (3004,'The Lord of the Rings','J.R.R Tolkien',37),
                     (3005,'Alice in Wonderland','Lewis Carroll',12)]

    cursor = db.cursor()
    cursor.executemany('''INSERT INTO books VALUES (?,?,?,?)''', initial_books)
    db.commit()


# Creating function called add_book for adding new books to database
def add_book():
    while True:
        while True:
            # Using try and except function here for id value
            try:
                Id = int(input(f"{YELLOW}Enter the book id: {END}"))

                cursor = db.cursor()
                cursor.execute("""SELECT * FROM books WHERE Id=?""", (Id,))
                if cursor.fetchone():
                    print(f"{RED}Book ID already exists in database.{END}")
                    continue
                else:
                    break
            except ValueError:
                print(f"{RED}Please enter a Integer!{END}")

        title = input(f"{YELLOW}Enter the book title: {END}")
        author = (input(f"{YELLOW}Enter the book author name: {END}"))
        while True:
            # using try and except function here for qty value
            try:
                qty = int(input(f"{YELLOW}Enter the book qty: {END}"))

                cursor.execute('''INSERT INTO books(Id, title, author, qty)
                                  VALUES(?,?,?,?)''', (Id, title, author, qty))
                db.commit()
                print(f"{GREEN}Book data added to database!{END}")
                main_menu()
            except ValueError:
                print(f"{RED}Please enter valid Quantity!{END}")


# Creating function called update_book for updating book data into database
def update_book():
    cursor = db.cursor()
    while True:

        update_option = input('''Select one of the following Options below to be updated(or enter 0 to main_menu)
        : Id, title, author, qty: ''').lower()

        # Update data by using id value
        if update_option == 'id':
            while True:
                # using try and except function here for id value
                try:
                    Id = int(input(f"{YELLOW}Enter the new id of book: {END}"))
                except ValueError:
                    print(f"{RED}Please enter a Integer!{END}")
                    continue
                if Id > 0:
                    cursor.execute("""SELECT * FROM books WHERE Id=?""", (Id,))
                    if cursor.fetchone():
                        print(f"{RED}Book ID already exists in database.{END}")
                    else:
                        break
                else:
                    print(f'{RED}Please enter valid Id number!{END}')
                    continue
            while True:
                # using try and except function here for  old id value
                try:
                    Id_old = input(f"{YELLOW}Enter the book old id: {END}")

                except ValueError:
                    print(f"{RED}Please enter a Integer!{END}")
                    continue
                if Id > 0:

                    cursor.execute("""SELECT * FROM books WHERE Id=?""", (Id_old,))
                    if cursor.fetchone():
                        cursor.execute('''UPDATE books SET id = ? WHERE Id = ? ''', (Id, Id_old,))
                        print(f'{GREEN}Book data has been updated!{END}')
                        db.commit()
                        main_menu()
                    else:
                        print(f"{RED}Please enter valid old Id number!!{END}")
                else:
                    print(f'{RED}Please enter valid old Id number!{END}')
                    continue



        # Update data by using title name
        elif update_option == 'title':
            while True:
                # using try and except function here for id value
                try:
                    Id = int(input(f"{YELLOW}Enter the book id to be updated: {END}"))
                except ValueError:
                    print(f"{RED}Please enter a Integer!{END}")
                    continue
                title = input(f"{YELLOW}Enter the new title of book: {END}")
                cursor = db.cursor()
                cursor.execute("""SELECT * FROM books WHERE Id=?""", (Id,))
                if cursor.fetchone():
                    cursor.execute('''UPDATE books SET title = ? WHERE Id = ? ''', (title, Id))
                    print(f'{GREEN}Book title has been updated!')
                    db.commit()
                    main_menu()
                else:
                    print(f"{RED}Please enter valid book id!{END}")
                    continue


        # Update data by using author name
        elif update_option == 'author':
            while True:
                # using try and except function here for id value
                try:
                    Id = int(input(f"{YELLOW}Enter the book id: {END}"))
                except ValueError:
                    print(f"{RED}Please enter a Integer!{END}")
                    continue
                while True:
                    author = (input(f"{YELLOW}Enter the new name of author: {END}"))
                    cursor = db.cursor()
                    cursor.execute("""SELECT * FROM books WHERE Id=?""", (Id,))
                    if cursor.fetchone():
                        cursor.execute('''UPDATE books SET author = ? WHERE Id = ? ''', (author, Id))
                        print(f'{GREEN}Book author data has been updated!')
                        db.commit()
                        main_menu()
                    else:
                        print(f"{RED}Please enter valid book id!{END}")
                        continue


        # Update data by using Quantity value
        elif update_option == 'qty':
            while True:
                # using try and except function here for id value
                try:
                    Id = int(input(f"{YELLOW}Enter the book id: {END}"))
                    cursor = db.cursor()
                    cursor.execute("""SELECT * FROM books WHERE Id=?""", (Id,))
                    if cursor.fetchone():
                        qty = int(input(f"{YELLOW}Enter the new quantity of book: {END}"))
                        cursor.execute('''UPDATE books SET qty = ? WHERE Id = ? ''', (qty, Id))
                        print(f'{GREEN}Book quantity has been updated!{END}')
                        db.commit()
                        main_menu()
                    else:
                        print(f'{RED}Enter valid book id{END}')
                except ValueError:
                    print(f"{RED}Please enter a Integer!{END}")
                    continue





        elif update_option == '0':
            main_menu()
        else:
            print(f"{RED}Invalid Option{END}")
            continue


# Creating function called delete_book for deleting book data from database
def delete_book():
    while True:
        # using try and except function here for id value
        try:
            Id = int(input(f"{YELLOW}Enter the book id to be deleted(press 0 to main menu): {END}"))
        except ValueError:
            print(f"{RED}Please enter a Integer!{END}")
            continue

        cursor = db.cursor()
        cursor.execute("""SELECT * FROM books WHERE Id=?""", (Id,))
        if cursor.fetchone():
            cursor.execute('''DELETE FROM books WHERE Id = ? ''', (Id,))
            print(f'Id %d deleted' % Id)
            print(f'{GREEN}Book data has been deleted!{END}')
            db.commit()
            main_menu()
        elif Id == 0:
            main_menu()
        else:
            print(f'{RED}No book found! Please enter valid id.{END}')
            continue


# Creating function called search_book for getting specific book from database
def search_book():
    cursor = db.cursor()
    while True:
        search_option = input('''Select one of the following Options below to search(or enter 0 to main menu):
         Id, title, author, qty: ''').lower()

        # Search data by using id value
        if search_option == 'id':
            while True:
                try:
                    Id = input(f"{YELLOW}Please enter the book ID: {END}")

                    cursor.execute('''SELECT * FROM books WHERE ID=?''', (Id,))
                    book = cursor.fetchone()

                    if book:
                        print(f"""{BLUE}\t\t\t\t\t\tBook ID: {book[0]}
                        title: {book[1]}
                        author: {book[2]}
                        Quantity: {book[3]}{END}""")
                        break

                    else:
                        print(f"{RED}Book not in database.{END}")
                except ValueError:
                    print(f"{RED}Please enter a Integer!{END}")
                    continue

        # Search data by using title name
        elif search_option == "title":
            while True:
                title = input(f"{YELLOW}Please enter the book title: {END}")

                cursor.execute('''SELECT * FROM books WHERE title=?''', (title,))
                book = cursor.fetchone()

                if book:
                    print(f"""\t\t\t\t\t\t{BLUE}Book ID: {book[0]}
                    title: {book[1]}
                    author: {book[2]}
                    Quantity: {book[3]}{END}""")
                    break

                else:
                    print(f"{RED}Book not in database.{END}")

        # Search data by using author name
        elif search_option == "author":
            while True:
                author = input(f"{YELLOW}Please enter the book author: {END}")
                cursor.execute('''SELECT * FROM books WHERE author=?''', (author,))
                book = cursor.fetchone()
                if book:
                    print(f"""\t\t\t\t\t\t{BLUE}Book ID: {book[0]}
                    title: {book[1]}
                    author: {book[2]}
                    Quantity: {book[3]}{END}""")
                    break
                else:
                    print(f"{RED}Book not in database.{END}")

        # Search data by using quantity value
        elif search_option == "qty":
            while True:
                try:
                    qty = input(f"{YELLOW}Please enter the book Quantity: {END}")

                    cursor.execute("""SELECT * FROM books WHERE qty=?""", (qty,))
                    book = cursor.fetchone()
                    if book:
                        print(f'''\t\t\t\t\t\t{BLUE}Book ID: {book[0]}
                        title: {book[1]}
                        author: {book[2]}
                        Quantity: {book[3]}{END}''')
                        break
                    else:
                        print(f"{RED}Book not in database.{END}")
                except ValueError:
                    print(f"{RED}Please enter a Integer!{END}")
                    continue

        elif search_option == "0":
            main_menu()
        else:
            print(f"{RED}You have entered wrong option! Try again!!{END}")
            continue


# Creating function called view_All for viewing all book from database
def view_all():
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM books''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print(f"{GREEN}Book data has been retrieved!{END}")

# Declaring colors and style to use throughout the program


END = "\33[0m"
RED = "\33[31m"
GREEN = "\33[32m"
YELLOW = "\33[33m"
BLUE = "\33[34m"


# --------Main MEnu-----------
def main_menu():
    while True:
        menu = input('''Select one of the following Options below: \33[1m \33[3m
                           1 - Add a book
                           2 - Update a book
                           3 - Delete a book
                           4 - Search a book
                           5 - View all books
                           6 - Exit  {END} 
                           : ''')
        if menu == "1":
            add_book()
        elif menu == "2":
            update_book()
        elif menu == "3":
            delete_book()
        elif menu == "4":
            search_book()
        elif menu == "5":
            view_all()
        elif menu == "6":
            print(f"{YELLOW}Goodbye!!!{END}")
            exit()
        else:
            print(f"{RED}You have made a wrong choice, Please Try again!!{END}")


# Initial calling function for creating database and main menu
create_db()
main_menu()