from banking_app.entities.user import User, PhoneContact, EmailContact
from banking_app.entities.vault import Vault


def test_user_init_has_no_contact():
    new_user = User(first_name="abc", last_name="def")
    assert new_user._contact_details == {"phone": None, "email": None}


def test_user_init_has_no_vault():
    new_user = User(first_name="abc", last_name="def")
    assert new_user.vault is None


def test_user_add_vault_overwrites_it():
    new_user = User(first_name="abc", last_name="def")
    new_user.add_vault(Vault(password="abc123"))
    first_vault = new_user.vault
    new_user.add_vault(Vault(password="abcxxx"))
    assert new_user.vault != first_vault
