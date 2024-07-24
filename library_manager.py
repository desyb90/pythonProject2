class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = {'title': title, 'author': author, 'year': year, 'status': 'available'}
        self.books.append(book)
        return "Book added successfully."

    def search_books(self, search_term):
        results = [book for book in self.books if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]
        return results

    def check_out_book(self, title, borrower):
        for book in self.books:
            if book['title'].lower() == title.lower() and book['status'] == 'available':
                book['status'] = 'checked out'
                book['borrower'] = borrower
                return "Book checked out successfully."
        return "Book not available or does not exist."

    def return_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and book['status'] == 'checked out':
                book['status'] = 'available'
                book.pop('borrower', None)
                return "Book returned successfully."
        return "Book not found or not checked out."

    def list_books(self):
        return self.books

def main_menu(test_mode=False):
    book_manager = BookManager()
    
    if test_mode:
        # Run predefined test actions
        print(book_manager.add_book("1984", "George Orwell", "1949"))
        print(book_manager.add_book("To Kill a Mockingbird", "Harper Lee", "1960"))
        print(book_manager.search_books("1984"))
        print(book_manager.check_out_book("1984", "John Doe"))
        print(book_manager.return_book("1984"))
        print(book_manager.list_books())
    else:
        while True:
            print("\nLibrary Menu:")
            print("1. Add Book")
            print("2. Search Book")
            print("3. Check Out Book")
            print("4. Return Book")
            print("5. List Books")
            print("6. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = input("Enter publication year: ")
                print(book_manager.add_book(title, author, year))
            
            elif choice == '2':
                search_term = input("Enter search term (title or author): ")
                results = book_manager.search_books(search_term)
                if results:
                    for book in results:
                        print(book)
                else:
                    print("No books found.")
            
            elif choice == '3':
                title = input("Enter book title to check out: ")
                borrower = input("Enter borrower name: ")
                print(book_manager.check_out_book(title, borrower))
            
            elif choice == '4':
                title = input("Enter book title to return: ")
                print(book_manager.return_book(title))
            
            elif choice == '5':
                books = book_manager.list_books()
                if books:
                    for book in books:
                        print(book)
                else:
                    print("No books in the library.")
            
            elif choice == '6':
                print("Exiting the library system.")
                break
            
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu(test_mode=True)  # Set test_mode to True for non-interactive mode
