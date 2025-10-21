from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "05253000723")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "05253000723"

    def test_pesel_too_long(self):
        account = Account("John", "Doe", "052530007231111")
        assert account.pesel == "Invalid"

    def test_pesel_too_short(self):
        account = Account("John", "Doe", "052530")
        assert account.pesel == "Invalid"
    
    def test_pesel_not_numeric(self):
        account = Account("John", "Doe", "ABC")
        assert account.pesel == "Invalid"

    def test_promo_code_valid(self):
        account = Account("John", "Doe", "ABC", "PROM_123")
        assert account.balance == 50.0

    def test_promo_code_invalid_format(self):
        account = Account("John", "Doe", "ABC", "1_345678")
        assert account.balance == 0.0

    def test_promo_code_wrong_prefix(self):
        account = Account("John", "Doe", "ABC", "PAOM_123")
        assert account.balance == 0.0
        
    def test_promo_code_wrong_suffix(self):
        account = Account("John", "Doe", "ABC", "PROM_5678")
        assert account.balance == 0.0

    def test_promo_code_wrong_suffix(self):
        account = Account("John", "Doe", "ABC", "PROM_5")
        assert account.balance == 0.0