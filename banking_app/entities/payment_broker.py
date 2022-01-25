from dataclasses import dataclass


@dataclass
class PaymentBroker:
    name: str
    earnings: int = 0

    def compensate_transaction_fee(self, fee: int):
        self.earnings += fee

    def revert_transaction_fee(self, fee: int):
        self.earnings -= fee
