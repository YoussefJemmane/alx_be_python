
class Book:
    """Represents a book with title, author, and checkout status."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author. Book starts as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books with checkout/return functionality."""
    
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """Add a Book instance to the library collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title if it's available.
        Marks the book as checked out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """
        Return a book by title.
        Marks the book as available.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available.")
            return
        
        for book in available_books:
            print(f"{book.title} by {book.author}")