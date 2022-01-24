from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict
from random import randint
from money_storage import MoneyStorage


def get_id() -> int:
    return randint(1000, 100000)


@dataclass
class Vault:
    password: str
    id: int = 0
    created_at: datetime = datetime.now()
    accounts: Dict[int, MoneyStorage] = field(default_factory=dict)

    def add_account(self, account: MoneyStorage) -> bool:
        print(account)
        if not isinstance(account, MoneyStorage):
            return False
        self.id = get_id()
        self.accounts[self.id] = account
        return True

    def get_accounts(self) -> Dict[int, str]:
        return {id: acc.name for id, acc in self.accounts.items()}

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
