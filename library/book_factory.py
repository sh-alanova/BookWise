from .book import Book
from typing import List

class BookFactory:
    def create_book(self, title: str, author: str, year: int, genre: str, tags: List[str] = None) -> Book:
        return Book(title, author, year, genre, tags)