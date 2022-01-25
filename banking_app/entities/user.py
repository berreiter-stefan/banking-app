from dataclasses import dataclass, field
from random import randint
from abc import ABC, abstractmethod
from typing import Dict
from datetime import datetime
from .vault import Vault


def get_id():
    return randint(100, 1000)


@dataclass
class Contact(ABC):
    ...

    def __post_init__(self):
        self.created_at: datetime = datetime.now()

    @abstractmethod
    def contact_info(self):
        ...


@dataclass
class EmailContact(Contact):
    email: str

    def contact_info(self):
        return self.email


@dataclass
class PhoneContact(Contact):
    prefix: str
    number: int

    def contact_info(self):
        return f"+{self.prefix}-{self.number}"


@dataclass
class User:
    first_name: str
    last_name: str
    _id: int = get_id()
    _contact_details: Dict[str, Contact] = field(
        default_factory=lambda: {"email": None, "phone": None}
    )
    _vault: Vault = None

    def add_contact(self, contact: Contact):
        if isinstance(contact, PhoneContact):
            self._contact_details["phone"] = contact
            return
        if isinstance(contact, EmailContact):
            self._contact_details["email"] = contact
            return
        raise NotImplementedError("Such a contact type is not implemented.")

    def add_vault(self, vault: Vault):
        self._vault = vault

    @property
    def vault(self):
        return self._vault
