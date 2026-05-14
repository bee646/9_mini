class Book:
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages must be a positive integer")
        self.pages = pages

    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages}p)"

   
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

   
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    
print("--- Part 1 ---")
try:
    books = [
        Book("Python Crash Course", "Eric Matthes", 544),
        Book("Clean Code", "Robert Martin", 431),
        Book("The Pragmatic Programmer", "David Thomas", 352),
        Book("Fluent Python", "Luciano Ramalho", 792)
    ]
    
    for book in books:
        print(book)

   
    invalid_book = Book("Invalid Book", "Unknown", -50)
except ValueError as e:
    print(f"ValueError: {e}")


print("\n--- Part 2 ---")

book_a = Book("Clean Code", "Robert Martin", 431)
book_b = Book("Clean Code", "Robert Martin", 100)
print(f"book_a == book_b: {book_a == book_b}")


print("--- Sorted by pages ---")
sorted_books = sorted(books)
for book in sorted_books:
    print(book)
