class PaymentBroker:

    def __init__(self, name: str):
        self.name: str = name
        self.earnings: int = 0

    def compensate_transaction_fee(self, fee: int):
        self.earnings += fee

    def revert_transaction_fee(self, fee: int):
        self.earnings -= fee
