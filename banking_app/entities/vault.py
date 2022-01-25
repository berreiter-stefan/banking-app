from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional
from random import randint
from .money_storage import MoneyStorage


def get_id() -> int:
    return randint(1000, 100000)


@dataclass
class Vault:
    password: str
    id: int = get_id()
    created_at: datetime = datetime.now()
    accounts: Dict[int, MoneyStorage] = field(default_factory=dict)

    def add_account(self, account: MoneyStorage) -> Optional[int]:
        if not isinstance(account, MoneyStorage):
            return None
        self.accounts[self.id] = account
        return self.id

    def get_accounts(self) -> Dict[int, str]:
        return {idx: acc.name for idx, acc in self.accounts.items()}

    def balance(self) -> int:
        return sum([account.balance for account in self.accounts.values()])

    def get_overview(self, password) -> None:
        if password != self.password:
            raise ValueError("Provided password is not your vault's password")

        print("---\nACCOUNT INFO ---")
        for id, account in self.accounts.items():
            print(f"Acc#{id} Details:")
            account.show_balance()
            print("---")
