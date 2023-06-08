from uuid import UUID
from dataclasses import dataclass


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
    