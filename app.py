
import json

# A file to store the library data
LIBRARY_FILE = "library.txt"

# This function loads the library data from the file library.txt.
# It reads the JSON data from the file and returns it as a list of books. If the file does not exist or the content is not valid JSON, it returns an empty list.
# The function is used to load the library data when the program starts. It is called in the main function.
def load_library():
    """Load the library from a file."""
    try:                                         # It uses a try-except block to handle possible errors.
        with open(LIBRARY_FILE, "r") as file:    # Opens the file in read mode. If the file doesn't exist, it will raise a FileNotFoundError
            return json.load(file)               # Load the JSON data from the file
    except (FileNotFoundError, json.JSONDecodeError): # If the file is not found (FileNotFoundError) or the content is not valid JSON (json.JSONDecodeError), it returns an empty list [] to avoid crashing the program.
        return []

# This function saves the current state of the library (list of books) to the file library.txt
def save_library(library):
    """Save the library to a file."""
    with open(LIBRARY_FILE, "w") as file:  ## It opens the file in write mode.
        json.dump(library, file, indent=4)  ## It writes the JSON data (library) to the file with an indentation of 4 spaces.


# This function adds a new book to the library.
# It prompts the user to enter the book details (title, author, year, genre, and read status) and creates a dictionary with this information.
def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {"title": title, "author": author, "year": int(year), "genre": genre, "read": read_status}
    library.append(book)   ## It appends the new book dictionary to the library list.
    print("Book added successfully!") ## It prints a success message to the user.

# This function removes a book from the library.
# It prompts the user to enter the title of the book to remove. It then searches for the book in the library and removes it if found.
def remove_book(library):
    """Remove a book from the library."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

#This function searches for a book in the library by title or author.
#It prompts the user to choose between searching by title or author and then enter the search term. It then searches for the book in the library and prints the details of the book if found.
def search_books(library):
    """Search for a book by title or by author."""
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    query = input("Enter search term: ").strip().lower() ## It prompts the user to enter the search term and converts it to lowercase for case-insensitive search.
    matches = [book for book in library if query in book["title"].lower() or query in book["author"].lower()] ## It searches for the query term in the title or author of each book in the library.
    
    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1): ## It prints the details of each matching book.
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}") ## It prints the book details with the index number.
    else:
        print("No matches found.") ## If no matches are found, it prints a message to inform the user.

#This function displays all the books in the library.
#It iterates over each book in the library and prints its details (title, author, year, genre, and read status).
def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Show library statistics."""
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.")
        return
    
    read_books = sum(1 for book in library if book["read"]) ## It counts the number of read books in the library.
    percentage_read = (read_books / total_books) * 100   ## It calculates the percentage of read books.
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

#This is the main function that runs the Personal Library Manager.
#It loads the library data from the file, displays the menu, and prompts the user to choose an option. It then calls the appropriate function based on the user's choice.
def main():
    """Main function to run the Personal Library Manager."""
    library = load_library()
    
    while True:
        print("""
        
        Welcome to your Personal Library Manager!
              
        * -----------M E N U-------------*
        *                                *
        *                                *      
        *    1. Add a book               *
        *    2. Remove a book            *
        *    3. Search for a book        *
        *    4. Display all books        *
        *    5. Display statistics       *
        *    6. Exit                     *
        *                                *          
        *                                *          
        * ---Developed By: Zahida Raees--*      

        """)
        choice = input("Enter your choice: ")
        
        
        if choice == "1":
            add_book(library)

        elif choice == "2":
            remove_book(library)

        elif choice == "3":
            search_books(library)

        elif choice == "4":
            display_books(library)

        elif choice == "5":
            display_statistics(library)

        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
#This line ensures that the main function is executed when the script is run.
if __name__ == "__main__":
    main()
