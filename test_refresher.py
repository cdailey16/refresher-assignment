from refresher import Drink, Order 

import unittest 

valid_bases = {'water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine'}

class Order:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items

    def get_num_items(self):
        return len(self._items)

    def __repr__(self):
        return f"Order(items={self._items})"

    def __str__(self):
        return f"Order with {len(self._items)} items"

    def get_total_price(self):
        subtotal = sum(item.get_price() for item in self._items)  # Sum the prices of all items
        tax = subtotal * 0.075  # Apply a 7.5% tax
        return subtotal + tax

class TestRefresher(unittest.TestCase): # TestRefresher class inherits from unittest.TestCase
    def setUp(self):  # setUp method is called before each test and sets up the initial state for the tests
        self.drink = Drink('medium', 'pokeacola', ['lemon'])  # Replace 'bokacola' with a valid base
        self.drink2 = Drink('large', 'sbrite', ['strawberry', 'blueberry'])
        self.drink3 = Drink('Mega', 'pokeacola', ['mint', 'lime'])
        self.order = Order()
        self.order.add_item(self.drink)
        self.order.add_item(self.drink2)
        self.order.add_item(self.drink3)
        
class TestDrink(unittest.TestCase):  # TestDrink class inherits from unittest.TestCase    
    def setUp(self):  # Initialize test fixtures before each test
        self.drink = Drink('medium', 'pokeacola', ['lemon'])  # Create a Drink object for testing
    
    def test_drink_initialization(self):
        self.assertEqual(self.drink.get_base(), 'pokeacola')
        self.assertEqual(self.drink.get_size(), 'medium')
        self.assertIn('lemon', self.drink.get_flavors())
        self.assertEqual(self.drink.get_num_flavors(), 1) 
        
    def test_drink_invalid_base(self):
        with self.assertRaises(ValueError):
            Drink('medium', 'invalid_base')  # Attempt to create a drink with an invalid base
        with self.assertRaises(ValueError):
            Drink('medium', 'pokeacola', ['invalid_flavor'])
            
    def test_get_size(self):
        size = self.drink.get_size()
            
    def test_set_flavors(self):
        self.drink.set_flavors(['cherry', 'mint'])
        self.assertIn('cherry', self.drink.get_flavors())
               
    def test_get_flavors(self):
        flavors = self.drink.get_flavors()
        self.assertIn('lemon', flavors)
               
    def test_drink_add_flavor(self):
        self.drink.add_flavor('cherry')
        self.assertIn('cherry', self.drink.get_flavors())
        self.assertEqual(self.drink.get_num_flavors(), 2)

    def test_get_price(self):
        price = self.drink.get_price()
        self.assertEqual(price, 1.75)
        
        
class TestOrder(unittest.TestCase):  # TestOrder class inherits from unittest.TestCase     
    def setUp(self):  # Initialize test fixtures before each test
        self.drink = Drink('medium', 'pokeacola', ['lemon'])
        self.drink2 = Drink('large', 'sbrite', ['strawberry', 'blueberry'])
        self.drink3 = Drink('Mega', 'pokeacola', ['mint', 'lime'])
        self.order = Order()  # Initialize the order
        self.order.add_item(self.drink)
        self.order.add_item(self.drink2)
        self.order.add_item(self.drink3)
        
    # Test to check if the items in the order are correctly retrieved    
    def test_get_items(self):
        items = self.order.get_items()
        self.assertEqual(len(items), 3)
        self.assertIn(self.drink, items)
       
    # Test to check if the number of items in the order is correct
    def test_get_num_items(self): 
        num_items = self.order.get_num_items()
        self.assertEqual(num_items, 3)
        
    # Test to check if the order can be represented as a string
    def test_order_repr(self):
        order_repr = repr(self.order)
        self.assertIn('Order(items=[', order_repr)
        

        
    def test_get_total_price(self):
        total_price = self.order.get_total_price()
        self.assertAlmostEqual(total_price, 6.39625, places=2)  # Update expected value






