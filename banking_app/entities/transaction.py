from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from random import randint
from abc import ABC, abstractmethod
from .payment_broker import PaymentBroker


TRANSACTION_FEE_PRCT: float = 0.00005


def get_id() -> int:
    return randint(1000, 100000)


@dataclass
class Transaction(ABC):
    sender_account: MoneyStorage
    receiver_account: MoneyStorage
    amount: int
    payment_broker: PaymentBroker = None
    transaction_fee: int = 0
    id: int = 0
    created_at: datetime = datetime.now()

    @abstractmethod
    def execute(self):
        ...

    @abstractmethod
    def undo(self):
        ...


@dataclass
class FreeTransaction(Transaction):
    def __post_init__(self):
        self.execute()

    def execute(self):
        self.id = get_id()
        self.sender_account.withdraw(self.amount)
        self.receiver_account.deposit(self.amount)
        print("normal executed")

    def undo(self):
        self.receiver_account.withdraw(self.amount)
        self.sender_account.deposit(self.amount)
        print("normal undone")


@dataclass
class PremiumTransaction(Transaction):
    def __post_init__(self):
        if not self.payment_broker:
            raise ValueError(
                "Payment Broker not specified for this Premium Transaction"
            )
        self.transaction_fee = int((1 - TRANSACTION_FEE_PRCT) * self.amount)
        self.net_amount = self.amount - self.transaction_fee
        self.execute()

    def execute(self):
        self.id = get_id()
        self.sender_account.withdraw(self.amount)
        self.receiver_account.deposit(self.net_amount)
        self.payment_broker.compensate_transaction_fee(self.transaction_fee)
        print("premium executed")

    def undo(self):
        self.receiver_account.withdraw(self.net_amount)
        self.sender_account.deposit(self.amount)
        self.payment_broker.revert_transaction_fee(self.transaction_fee)
        print("premium undone")
