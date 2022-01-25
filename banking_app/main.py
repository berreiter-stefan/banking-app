from entities.vault import Vault
from entities.money_storage import BankAccount, CryptoWallet, TransactionType
from entities.payment_broker import PaymentBroker
from entities.user import User, EmailContact, PhoneContact


def main():
    paypal = PaymentBroker(name="Paypal")

    user1 = User(first_name="Thomas", last_name="Mittelberger")
    user1.add_contact(EmailContact("thomas@gmail.com"))
    user1.add_contact(PhoneContact(prefix="43", number=1234333))
    user1.add_vault(Vault(password="vault1_pw"))
    user1_acc1_id = user1.vault.add_account(
        BankAccount(institute="Institute1", iban="1234567-abc")
    )
    user1.vault.accounts[user1_acc1_id].deposit(10000)

    user2 = User(first_name="Tamara", last_name="Brings")
    user2.add_contact(EmailContact("tamara@outlook.com"))
    user2.add_vault(Vault(password="vault2_pw"))
    user2_acc1_id = user2.vault.add_account(
        BankAccount(institute="N26", iban="111111-abc")
    )

    user1.vault.accounts[user1_acc1_id].send_money(
        receiver=user2.vault.accounts[user2_acc1_id], amount=1330
    )

    user2.vault.accounts[user2_acc1_id].send_money(
        receiver=user1.vault.accounts[user1_acc1_id],
        amount=250,
        t_type=TransactionType.PREMIUM,
        payment_broker=paypal,
    )

    user1.vault.get_overview(password="vault1_pw")
    user2.vault.get_overview(password="vault2_pw")

    print(f"paypal earnings so far: {paypal.earnings}")


if __name__ == "__main__":
    main()
