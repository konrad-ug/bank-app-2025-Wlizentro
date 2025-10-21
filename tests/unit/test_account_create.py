from src.account import Account
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

class TestAccount:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "05253000723")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "05253000723"

    def test_pesel_too_long(self):
        account = PersonalAccount("John", "Doe", "052530007231111")
        assert account.pesel == "Invalid"

    def test_pesel_too_short(self):
        account = PersonalAccount("John", "Doe", "052530")
        assert account.pesel == "Invalid"
    
    def test_pesel_not_numeric(self):
        account = PersonalAccount("John", "Doe", "ABC")
        assert account.pesel == "Invalid"

    def test_promo_code_valid(self):
        account = PersonalAccount("John", "Doe", "ABC", "PROM_123")
        assert account.balance == 50.0

    def test_promo_code_invalid_format(self):
        account = PersonalAccount("John", "Doe", "ABC", "1_345678")
        assert account.balance == 0.0

    def test_promo_code_wrong_prefix(self):
        account = PersonalAccount("John", "Doe", "ABC", "PAOM_123")
        assert account.balance == 0.0
        
    def test_promo_code_wrong_suffix(self):
        account = PersonalAccount("John", "Doe", "ABC", "PROM_5678")
        assert account.balance == 0.0

    def test_promo_code_wrong_suffix(self):
        account = PersonalAccount("John", "Doe", "ABC", "PROM_5")
        assert account.balance == 0.0

    def test_promo_older_then_max_promo(self):
        account = PersonalAccount("John", "Doe", "05253000723", "PROM_111")
        assert account.balance == 50.0
    
    def test_promo_younger_then_max_promo(self):
        account = PersonalAccount("John", "Doe", "59253000723", "PROM_111")
        assert account.balance == 0.0

class TestTransfers:
    def test_imcoming_transfer(self):
        account = Account("John", "Doe", "05253000723")
        account.incoming_transfer(100.0)
        assert account.balance == 100.0

    def test_outgoing_transfer(self):
        account = Account("John", "Doe", "05253000723")
        account.incoming_transfer(100.0)
        account.outgoing_transfer(60.0)
        assert account.balance == 40.0

    def test_not_enough_for_outgoing_transfer(self):
        account = Account("John", "Doe", "05253000723")
        account.incoming_transfer(100.0)
        account.outgoing_transfer(101.0)
        assert account.balance == 100.0

    def test_outgoing_transfer_not_numeric(self):
        account = Account("John", "Doe", "ABC")
        account.incoming_transfer(100.0)
        account.outgoing_transfer("abc")
        assert account.balance == 100.0
        # account.incoming_transfer(100.0)
        # lub
        # account.balance = 100.0
        # account.outgoing_transfer(60.0)

class TestCompanyAccount:
    def test_company_account_creation(self):
        account = CompanyAccount("Hossa", "1234567890")
        assert account.company_name == "Hossa"
        assert account.nip == "1234567890"
    
    def test_nip_too_long(self):
        account = CompanyAccount("Hossa", "12345678901")
        assert account.nip == "Invalid"
    
    def test_nip_too_short(self):
        account = CompanyAccount("Hossa", "052530")
        assert account.nip == "Invalid"
    
    def test_nip_not_numeric(self):
        account = CompanyAccount("Hossa", "ABC")
        assert account.nip == "Invalid"