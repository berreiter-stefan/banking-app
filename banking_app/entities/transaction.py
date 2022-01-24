from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from random import randint


def get_id() -> int:
    return randint(1000, 100000)


@dataclass
class Transaction:
    sender_account: MoneyStorage
    receiver_account: MoneyStorage
    amount: int
    id: int = 0
    created_at: datetime = datetime.now()

    def __post_init__(self):
        self.execute()

    def execute(self):
        self.id = get_id()
        self.sender_account.withdraw(self.amount)
        self.receiver_account.deposit(self.amount)
        print("executed")

    def undo(self):
        self.receiver_account.withdraw(self.amount)
        self.sender_account.deposit(self.amount)
        print("undo")
