#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.total = 0
        self.last_transaction_amount = 0
        self.discount = discount

    def add_item(self, item_name, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.last_transaction_amount = item_cost
        self.items.append({"item": item_name, "price": price, "quantity": quantity})

    def apply_discount(self):
        if self.discount >= 0 and self.discount <= 100:
            discount_factor = 1 - self.discount / 100
            self.total *= discount_factor
            return self.total
        else:
            return "Invalid discount percentage"

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction_amount
            self.items.pop()
            self.last_transaction_amount = 0
        else:
            return "No transactions to void"
