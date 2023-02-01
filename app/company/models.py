from enum import Enum

from pydantic import BaseModel, Field


class BusinessForm(Enum):
    sole_trader = "sole_trader"


class Company(BaseModel):
    name: str
    org_number: str
    business_form: BusinessForm
    sni: list[str] = Field([])
    tax_account: str


class Tax(BaseModel):
    pass


class PreliminaryTax(Tax):
    pass


class Transaction(BaseModel):
    pass
