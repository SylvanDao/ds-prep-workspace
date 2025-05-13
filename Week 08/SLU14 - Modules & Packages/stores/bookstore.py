
class Book:
    def __init__(self, title: str, author: str, price: int):
        self.title = title
        self.author = author
        self.price = price

    def get_book_info(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}."

def get_total_price(books: list['Book']) -> int: # Using 'Book' for forward reference compatibility
    total = 0
    for book_item in books:
        total += book_item.price
    return total

description = "This is a module named bookstore."
