from errno import errorcode
import mysql.connector
from  mysql.connector import errorcode

## Define congifuration for the database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

## Try to connect to the database, handle invalid credentials and bad DB
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

## show_meu method prints the main menu
def show_menu():
    print("-- MAIN MENU --")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Quit")
    print("")

## show_book method displays the books available at whatabook
def show_book(_cursor):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    for book in books:
        print("Book ID:{}       Book Name: {}".format(book[0], book[1]))

## show_locations method displays the whatabook locations
def show_locations(_cursor):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM store")
    stores = cursor.fetchall()
    for store in stores:
        print("Store Address: {}".format(store[1]))

## validate_user method returns true if the user is valid
def validate_user(_user_id):
    if _user_id == 1:
        return True
    elif _user_id == 2:
        return True
    elif _user_id == 3:
        return True
    else:
        return False    

## show_account_menu method displays the account menu after the user has been validated
def show_account_menu():
    print("-- ACCOUNT MENU --")
    print("1. Show wishlist")
    print("2. Add book")
    print("3. Main menu")

## show_wishlist method displays the wishlist for the specified user
def show_wishlist(_cursor, _user_id):
    cursor = db.cursor()
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = cursor.fetchall()

    for book in wishlist:
        print("Book Name: {}        Author: {}".format(book[4], book[5]))

## show_books_to_add method displays the books that are not in the user's wishlist
def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    cursor = db.cursor()
    cursor.execute(query)

    books_to_add = cursor.fetchall()

    for book in books_to_add:
        print("Book Id: {}        Book Name: {}".format(book[0], book[1]))

## add_books_to_wishlist method adds the specified book to the specified user's wishlist DB
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    cursor = db.cursor()
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

## Beginning of program code

## Initialize variables and show menu
show_menu()
selection = int(input("Please enter a selection: "))
acctSelection = 0
user_id = 0

## While loop ends if user selects 4, or quit
while selection != 4:
    ## Calls show_book method to display catalog
    if selection == 1:
        cursor = db.cursor
        show_book(cursor)
    ## Calls show_locations method to display whatabook locations
    elif selection == 2:
        cursor = db.cursor
        show_locations(cursor)
    ## Allows user to validate their ID and manipulate their wishlist
    elif selection == 3:
        user_id = int(input("Enter your user ID: "))
    ## Proceeds if user is valid
        if validate_user(user_id):
            show_account_menu()
        else:
            print("The user ID is not valid")
            break
        acctSelection = int(input("Enter a selection: "))
    ## While loop ends when user selects 3, or main menu
        while acctSelection != 3:
        ## Calls the show_wishlist method to show the user's wishlist
            if acctSelection == 1:
                cursor = db.cursor
                show_wishlist(cursor, user_id)
        ## Calls the show_books_to_add method and the add_books_to_wishlist method to allow user to add books
            elif acctSelection == 2:
                cursor = db.cursor
                show_books_to_add(cursor, user_id)
                book_id = int(input("Enter a book ID to add it to the wishlist: "))
                add_book_to_wishlist(cursor, user_id, book_id)
            elif acctSelection < 0 or acctSelection > 3:
                print("That is not a valid option. Please make a selection from the menu")
            show_account_menu()
            acctSelection = int(input("Enter a selection: "))
    elif selection < 0 or selection > 4:
        print("That is not a valid option. Please make a selection from the menu")
    show_menu()
    selection = int(input("Please enter a selection: "))

print("Thank you for using the Whatabook program. Have a good day!")
    