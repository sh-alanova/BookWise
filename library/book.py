from datetime import datetime
from typing import List, Any, Optional

class ValidatedString:
    def __init__(self, min_len=1):
        self.min_len = min_len
        self.name = None

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, "")

    def __set__(self, obj, value):
        if not isinstance(value, str) or len(value) < self.min_len:
            raise ValueError(f"{self.name} must be non-empty string")
        setattr(obj, self.name, value)

class BookMeta(type):
    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)

class Book(metaclass=BookMeta):
    title = ValidatedString()
    author = ValidatedString()

    def __init__(self, title: str, author: str, year: int, genre: str, tags: List[str] = None):
        self.title = title
        self.author = author
        self._year = year
        self._genre = genre
        self._tags = tags or []
        self._status = "не начата"
        self._last_opened: Optional[datetime] = None

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: Any):
        if not isinstance(value, int):
            raise TypeError("Year must be int")
        self._year = value

    def mark_as_read(self) -> None:
        self._status = "прочитана"
        self._last_opened = datetime.now()

    def add_tag(self, tag: str) -> None:
        if isinstance(tag, str) and tag not in self._tags:
            self._tags.append(tag)

    def __str__(self) -> str:
        return f"«{self.title}» by {self.author}"

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r})"

    def __eq__(self, other: Any) -> bool:
        if not hasattr(other, 'title') or not hasattr(other, 'author'):
            return False
        return self.title == other.title and self.author == other.author