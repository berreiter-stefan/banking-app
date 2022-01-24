from entitities.vault import Vault
from entitities.money_storage import BankAccount, CryptoWallet


def main():
    print("Create a Bank Account")
    vault = Vault(password="abc123")
    vault.add_account(BankAccount(institute="Institute1", iban="1234567-abc"))
    vault.add_account(CryptoWallet(currency="Bitcoin"))
    vault.get_overview(password="abc123")

    print(vault.get_accounts())


if __name__ == "__main__":
    main()
