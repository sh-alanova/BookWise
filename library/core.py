import json
import os
from typing import Generator, List, Iterator, Union
from .book import Book
from .decorators import LoggingDecorator

log_decorator = LoggingDecorator("Library")

class Library:
    def __init__(self):
        self._books: List[Book] = []

    @log_decorator
    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> bool:
        for i, book in enumerate(self._books):
            if book.title == title:
                del self._books[i]
                return True
        return False

    def search_by_tag(self, tag: str) -> Generator[Book, None, None]:
        matching = (book for book in self._books if tag in book._tags) 
        yield from matching

    def get_statistics(self) -> dict:
        if not self._books:
            return {}
        total = len(self._books)
        read = len([b for b in self._books if b._status == "прочитана"])
        avg_year = sum(b.year for b in self._books) / total
        return {"total": total, "read": read, "avg_year": avg_year}

    def export_to_json(self) -> None:
        path = os.getenv("LIBRARY_PATH", "library.json")
        dir_path = os.path.dirname(path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True) 

        data = [{
            "title": b.title,
            "author": b.author,
            "year": b.year,
            "genre": b._genre,
            "tags": b._tags,
            "status": b._status
        } for b in self._books]

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)