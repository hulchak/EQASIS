class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"

    def is_available(self):
        return not self.is_checked_out

book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book.get_info())
print("Available:", book.is_available())
print("Check out:", book.check_out())
print("Available after check out:", book.is_available())
