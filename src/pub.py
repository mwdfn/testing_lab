
class Pub:
    def __init__(self, name, till_value):
        self.name = name
        self.till_value = till_value
        self.drinks = []

    def drinks_list(self):
        return len(self.drinks)

    def add_money_to_till(self, price):
        self.till_value += price

    