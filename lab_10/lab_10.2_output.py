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

class BookDetails:

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.condition = "Good"

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"

    def check_condition(self):
        return self.condition

class EnhancedLibraryBook:

    def __init__(self, title, author, publication_year):
        self.book_details = BookDetails(title, author, publication_year)
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

    def get_book_info(self):
        return self.book_details.get_info()

    def get_book_condition(self):
        return self.book_details.check_condition()

# Використання коду
enhanced_book = EnhancedLibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(enhanced_book.check_out())
print(enhanced_book.check_out())
print(enhanced_book.get_book_info())
print(enhanced_book.get_book_condition())
