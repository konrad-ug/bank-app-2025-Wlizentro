class Account:
    def incoming_transfer(self, amount):
        if amount > 0:
            self.balance += amount

    def outgoing_transfer(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

    # def is_more_then_max_age(self, pesel):
    #     print(pesel[0] + pesel[1])
    #     if int(pesel[0] + pesel[1]) < 60:
    #       return True
    #     return False

