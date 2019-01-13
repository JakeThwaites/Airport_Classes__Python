class Passenger:
    def __init__(self, name, money):
        self.name = name;
        self.money = money

    def buy_ticket(self):
        self.money -= 5

