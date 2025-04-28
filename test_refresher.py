from refresher import Drink, Order # Importing the Drink and Order classes from refresher.py

import unittest #import unittest.mock import patch <-- This line is not needed as we are not using patch in this test

## Test code for refresher.py ##
class TestRefresher(unittest.TestCase): # TestRefresher class inherits from unittest.TestCase
    def setUp(self): # setUp method is called before each test and sets up the initial state for the tests
        
        
        # Initialize an Order instance and two Drink instances with flavors and add them to the order
        self.order = Order()
        self.drink1 = Drink('water')
        self.drink1.set_flavors(['lemon', 'cherry'])
        self.drink2 = Drink('sbrite')
        self.drink2.set_flavors(['strawberry', 'blueberry'])
        self.order.add_item(self.drink1)
        self.order.add_item(self.drink2)
        
        
    # Test to check if the order is empty initially
    def test_order_initially_empty(self):
        order = Order()
        self.assertEqual(order.get_num_items(), 0)
        
        
     # Test to check if the items in the order are correctly retrieved    
    def test_get_items(self):
        items = self.order.get_items()
        self.assertEqual(len(items), 2)
        self.assertIn(self.drink1, items)
        self.assertIn(self.drink2, items)

    # Test to check if the number of items in the order is correct
    def test_get_num_items(self): 
        num_items = self.order.get_num_items()
        self.assertEqual(num_items, 2)
    
    drink1 = Drink('water')
    drink1.set_flavors(['lemon', 'cherry'])
    drink2 = Drink('sbrite')
    drink2.set_flavors(['strawberry', 'blueberry'])
    order = Order()
    order.add_item(drink1)
    order.add_item(drink2)
    
    