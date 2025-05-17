class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            return f"After the discount, the total comes to ${int(self.total)}.\n"
        else:
            return "There is no discount to apply.\n"

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        # You can improve removing last transaction items here if needed
        self.last_transaction_amount = 0
