from abc import ABC, abstractmethod


class Database(ABC):
    """Abstract class for database methods"""
    def __init__(self, source):
        self.database = source

    @abstractmethod
    def read_db(self):
        pass

    @abstractmethod
    def save_db(self, updates):
        pass

