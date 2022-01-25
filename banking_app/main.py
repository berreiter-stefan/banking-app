from entities.vault import Vault
from entities.money_storage import BankAccount, CryptoWallet, TransactionType
from entities.payment_broker import PaymentBroker


def main():
    print("Create a Payment Provider")
    paypal = PaymentBroker(name="Paypal")
    print(f"paypal earnings so far: {paypal.earnings}")

    print("Create a Bank Account")
    vault1 = Vault(password="vault1_pw")
    vault1_acc_id = vault1.add_account(
        BankAccount(institute="Institute1", iban="1234567-abc")
    )
    vault1.add_account(CryptoWallet(currency="Bitcoin"))
    vault1.accounts[vault1_acc_id].deposit(10000)
    #vault1.get_overview(password="vault1_pw")

    vault2 = Vault(password="vault2_pw")
    vault2_acc_id = vault2.add_account(BankAccount(institute="N26", iban="111111-abc"))

    vault1.accounts.get(vault1_acc_id).send_money(
        receiver=vault2.accounts.get(vault2_acc_id), amount=133
    )
    vault1.accounts.get(vault1_acc_id).send_money(
        receiver=vault2.accounts.get(vault2_acc_id), amount=200, t_type=TransactionType.PREMIUM, payment_broker=paypal
    )

    vault1.accounts.get(vault1_acc_id).send_money(
        receiver=vault2.accounts.get(vault2_acc_id), amount=1000, t_type=TransactionType.PREMIUM, payment_broker=paypal
    )

    #vault1.get_overview(password="vault1_pw")
    #vault2.get_overview(password="vault2_pw")
    #vault1.accounts.get(vault1_acc_id).revert_past_money_transfer()
    #vault1.accounts.get(vault1_acc_id).revert_past_money_transfer()

    #vault1.get_overview(password="vault1_pw")
    #vault2.get_overview(password="vault2_pw")

    print(f"paypal earnings so far: {paypal.earnings}")


if __name__ == "__main__":
    main()
