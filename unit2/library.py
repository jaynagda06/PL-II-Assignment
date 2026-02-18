class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self):
        self.available = True
        print("Book returned")

    def display(self):
        print(self.book_name, "-", self.author, "| Available:", self.available)

book = Library("Python Basics", "Guido")
book.display()
book.check_out()
book.return_book()
