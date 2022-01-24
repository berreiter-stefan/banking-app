import pytest
from banking_app.entities.money_storage import BankAccount


def test_if_account_empty_after_init():
    acc = BankAccount(institute="Institute1", iban="1234567-abc")
    assert acc.balance == 0, "account balance must be 0 after initializing"


def test_if_account_can_be_overdrawn():
    acc = BankAccount(institute="Institute1", iban="1234567-abc")
    with pytest.raises(ValueError):
        acc.withdraw(
            amount=100
        ), "should not be possible to withdraw money from an empty account."

