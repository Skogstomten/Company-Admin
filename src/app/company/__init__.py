from enum import Enum
from dataclasses import dataclass


class BusinessForm(Enum):
    sole_trader = "sole_trader"


@dataclass
class Company:
    name: str
    business_form: BusinessForm
    tax_account: str
    org_number: str
    sni: list[str]
