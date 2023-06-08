from enum import Enum
from dataclasses import dataclass

from pydantic import BaseModel, Field


class BusinessForm(Enum):
    sole_trader = "sole_trader"


@dataclass
class Company(BaseModel):
    name: str
    business_form: BusinessForm = BusinessForm.sole_trader
    tax_account: str = ""
    org_number: str = ""
    sni: list[str] = Field([])
