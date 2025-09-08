import logging
from typing import Callable, Any

class LoggingDecorator:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)

    def log_call(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            self.logger.info(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper