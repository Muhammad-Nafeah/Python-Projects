import os

file_name = "library.txt"

# Load existing library data from file (if it exists)
def load_library_from_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                book_data = line.strip().split(",")
                if len(book_data) == 5:
                    book: dict = {
                        "title": book_data[0],
                        "author": book_data[1],
                        "publication_year": int(book_data[2]),
                        "genre": book_data[3],
                        "read_status": book_data[4]
                    }
                    library.append(book)

# Save current library state to file
def save_book_to_file():
    with open(file_name, "w") as file:
        for book in library:
            line = f"{book['title']},{book['author']},{book['publication_year']},{book['genre']},{book['read_status']}\n"
            file.write(line)

# List to store books as dictionaries
library: list = []

# Display menu options to the user
def display_menu():
    print("\n*********Welcome to the Personal Library Manager*********")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display Statistics")
    print("6. Exit")

# Add a new book to the library
def add_book():
    book_title: str = input("Enter the title of the book:\n")
    book_author: str = input("Enter the author of the book:\n")
    book_publication_year: int = int(input("Enter the publication year of the book:\n"))
    book_genre: str = input("Enter the genre of the book:\n")
    book_read_status: str = input("Enter the read status of the book (Type 'read' for yes and 'unread' for no):\n")

    book: dict = {
        "title": book_title,
        "author": book_author,
        "publication_year": book_publication_year,
        "genre": book_genre,
        "read_status": book_read_status
    }
    library.append(book)
    print("Book Added Successfully!")
    save_book_to_file()

# Remove a book by title
def remove_book():
    book_title: str = input("Enter the title of the book to be removed:\n")

    for book in library:
        if book["title"].lower() == book_title.lower():
            library.remove(book)
            print(f"The Book {book_title} Removed Successfully")
            save_book_to_file()
            return
    print(f"The Book {book_title} Not Found in the Library")

# Search for a book by title or author
def search_book():
    print("Search Book By:\n 1. Title\n 2. Author")
    choice: int = int(input("Enter Your Choice (1 - 2):\n"))

    match choice:
        case 1:
            book_title: str = input("Enter the title of the book to be searched:\n")
            for index, book in enumerate(library, start=1):
                if book["title"].lower() == book_title.lower():
                    print("Matching Books:\n")
                    print(f'{index}. {book["title"].upper()} by {book["author"].upper()} ({book["publication_year"]}) - {book["genre"].capitalize()} - {book["read_status"].capitalize()}\n')
                    return
            print(f"The book {book_title.capitalize()} Not Found in the Library")

        case 2:
            book_author: str = input("Enter the author of the book to be searched:\n")
            for index, book in enumerate(library, start=1):
                if book["author"].lower() == book_author.lower():
                    print("Matching Books:\n")
                    print(f'{index}. {book["title"].upper()} by {book["author"].upper()} ({book["publication_year"]}) - {book["genre"].capitalize()} - {book["read_status"].capitalize()}\n')
                    return
            print(f"The Author {book_author.capitalize()} Not Found in the Library")
        case _:
            print("Invalid Choice")

# Display all books currently in the library
def display_all_books():
    if not library:
        print("The Library is Empty!")
    else:
        print("Displaying all Books in the Library:\n")
        for index, book in enumerate(library, start=1):
            print(f"{index}. {book['title'].upper()} by {book['author'].upper()} ({book['publication_year']}) - {book['genre'].capitalize()} - {book['read_status'].capitalize()}\n")

# Show statistics like total and percentage of read books
def display_statistics():
    total_books = len(library)
    print(f"Total Books in the Library: {total_books}\n")

    if total_books == 0:
        print("No books in the library to calculate statistics.")
        return

    read_books = 0
    for book in library:
        if book["read_status"].lower() == "read":
            read_books += 1
    percentage = (read_books / total_books) * 100
    print(f"Percentage of Read Books: {percentage:.2f}%")

# Save and exit the application
def exit_program():
    save_book_to_file()
    print("Thank you for using the Personal Library Manager!")
    quit()

# Main loop to run the program
def main():
    load_library_from_file(file_name)
    while True:
        display_menu()
        choice: int = int(input("Enter Your Choice (1 - 6): \n"))

        match choice:
            case 1:
                add_book()
            case 2:
                remove_book()
            case 3:
                search_book()
            case 4:
                display_all_books()
            case 5:
                display_statistics()
            case 6:
                exit_program()
            case _:
                print("Invalid Choice")

main()
