import logging
from dotenv import load_dotenv
import os
from library.core import Library
from library.book_factory import BookFactory
from library.plugins.plugin_loader import PluginLoader

load_dotenv()

logging.basicConfig(
    level=getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper()),
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
)

logger = logging.getLogger("BookWise.Main")

def main():
    logger.info("Инициализация библиотеки...")
    lib = Library()

    factory = BookFactory()
    book1 = factory.create_book("1984", "Оруэлл", 1949, "Антиутопия", ["классика"])
    book2 = factory.create_book("Мастер и Маргарита", "Булгаков", 1967, "Роман", ["магия", "сатира"])

    lib.add_book(book1)
    lib.add_book(book2)

    loader = PluginLoader(os.getenv("PLUGIN_DIR", "plugins/"))
    loader.load_plugins()  # ❗ метод есть, но пустой

    fantasy_books = lib.search_by_tag("классика")
    for book in fantasy_books:
        print(f"Найдено: {book}")

    lib.export_to_json()

if __name__ == "__main__":
    main()