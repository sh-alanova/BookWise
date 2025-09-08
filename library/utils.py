from contextlib import contextmanager
from typing import Any

@contextmanager
def library_transaction(library: Any):
    backup = library._books[:]
    try:
        yield library
    except Exception:
        library._books = backup
        raise