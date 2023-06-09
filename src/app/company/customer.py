from uuid import UUID
from dataclasses import dataclass

from app.db import Database


@dataclass
class Customer:
    id: UUID
    name: str
    nin: str
    email: str
    co_address: str | None
    street_address: str
    zip_code: str
    city: str


class CustomerService:
    def __init__(self, db: Database):
        self.db = db

    def add_customer(self, customer: Customer) -> Customer:
        return self.db.collection("customers").add(customer)
