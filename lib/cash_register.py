class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([(title, price, quantity)])

    def apply_discount(self):
        if self.discount > 0:
            discounted_total= self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${discounted_total:.2f}")
            self.total = discounted_total
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_transaction_price = sum(price * quantity for _, price, quantity in self.items[::-1] if price)
            self.total -= last_transaction_price
            self.items.pop()
            