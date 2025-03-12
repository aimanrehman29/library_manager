import json

LIBRARY_FILE = "library.json"

def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    while True:
        try:
            year = int(input("Enter the publication year: ").strip())
            break
        except ValueError:
            print("Invalid year. Please enter a valid number.")

    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read_status
    }

    library.append(book)
    save_library(library)
    print("Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    found = False

    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("Book removed successfully!")
            found = True
            break

    if not found:
        print("Book not found in the library.")

def search_book(library):
    print("Search by: \n1. Title\n2. Author")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        search_key = "Title"
    elif choice == "2":
        search_key = "Author"
    else:
        print("Invalid choice!")
        return

    search_value = input(f"Enter the {search_key.lower()}: ").strip().lower()
    matching_books = [book for book in library if search_value in book[search_key].lower()]

    if matching_books:
        print("\nMatching Books:")
        for idx, book in enumerate(matching_books, start=1):
            status = "Read" if book["Read"] else "Unread"
            print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")
    else:
        print("No matching books found.")

def display_books(library):
    if not library:
        print("Your library is empty.")
        return

    print("\nYour Library:")
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["Read"] else "Unread"
        print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library yet.")
        return

    read_books = sum(1 for book in library if book["Read"])
    read_percentage = (read_books / total_books) * 100

    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_percentage:.2f}%")

def main():
    library = load_library()

    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            save_library(library)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

# cmd "Get-Content library.json | ConvertFrom-Json | Format-List"   powershwll  (to check library.json)