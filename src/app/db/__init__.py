from abc import ABCMeta, abstractmethod


class DatabaseCollection(metaclass=ABCMeta):
    """Represents a collection of documents."""


class Database(metaclass=ABCMeta):
    @abstractmethod
    def collection(
        self, collection_name: str
    ) -> DocumentDatabaseCollection:
        """Get collection by name."""
