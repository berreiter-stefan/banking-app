from abc import ABC, abstractmethod
from random import randint


def get_id() -> int:
    return randint(0, 100)


def generate_wallet_address() -> str:
    return f"some-address-{randint(0, 10000):05}"


class MoneyStorage(ABC):
    def __init__(self):
        self.id: int = get_id()
        self.balance: int = 0
        self.currency: str = ""
        self.name: str = "undefined"

    @abstractmethod
    def deposit(self, amount: int) -> None:
        ...

    @abstractmethod
    def withdraw(self, amount: int) -> None:
        ...

    @abstractmethod
    def show_balance(self) -> None:
        ...


class BankAccount(MoneyStorage):
    def __init__(self, institute: str, iban: str):
        super().__init__()
        self.currency: str = "€"
        self.bank_institute: str = institute
        self.iban: str = iban
        self.name: str = f"Bank Account with iban: {iban[:5]}-xxx"

    def withdraw(self, amount: int) -> None:
        if self.balance < amount:
            raise ValueError("Too little money on the account")
        self.balance -= amount

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("You cannot deposit negative money")
        self.balance += amount

    def show_balance(self) -> None:
        print(
            f"Balance of {self.iban} @{self.bank_institute}:\n{self.balance} {self.currency}"
        )


class CryptoWallet(MoneyStorage):
    def __init__(self, currency: str):
        super().__init__()
        self.wallet_address: str = generate_wallet_address()
        self.currency: str = currency
        self.name = f"Wallet @{self.wallet_address}"

    def withdraw(self, amount: int) -> None:
        if self.balance < amount:
            raise ValueError("Too little money on the account")
        self.balance -= amount

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("You cannot deposit negative money")
        self.balance += amount

    def show_balance(self) -> None:
        print(f"Balance of {self.wallet_address}: {self.balance} {self.currency}")
