#!/usr/bin/env python3
import io
import sys
import unittest
from cash_register import CashRegister

class TestCashRegister(unittest.TestCase):
    '''CashRegister in cash_register.py'''

    def setUp(self):
        self.cash_register = CashRegister()
        self.cash_register_with_discount = CashRegister(20)

    def reset_register_totals(self):
        self.cash_register.total = 0
        self.cash_register_with_discount.total = 0

    def test_discount_attribute(self):
        '''takes one optional argument, a discount, on initialization.'''
        self.assertEqual(self.cash_register.discount, 0)
        self.assertEqual(self.cash_register_with_discount.discount, 20)

    def test_total_attribute(self):
        '''sets an instance variable total to zero on initialization.'''
        self.assertEqual(self.cash_register.total, 0)
        self.assertEqual(self.cash_register_with_discount.total, 0)

    def test_items_attribute(self):
        '''sets an instance variable items to an empty list on initialization.'''
        self.assertEqual(self.cash_register.items, [])
        self.assertEqual(self.cash_register_with_discount.items, [])

   

if __name__ == '__main__':
    unittest.main()
