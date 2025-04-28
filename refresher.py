# refresher.py Assignment
class Order: # Order class to manage drink items in an order
    def __init__(self):
        self._items = []  # Private empty list to store drink items

# Get items getter function to return the list of items and return list of drink items
    def get_items(self):  
        return self._items

 # Get total getter function to return the total number of items in the order
    def get_total(self):
        return len(self._items)  

 # Get num items getter function to return the number of items in the order
    def get_num_items(self):  
        return len(self._items)

# Get receipt function to return a formatted string of all drink items in the order
    def get_receipt(self): 
        receipt = []
        for drink in self._items:
            receipt.append(str(drink))
        return "\n".join(receipt)

    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]
     
            
class Drink:
    def __init__(self, base):
        self._base = base
        self._flavors = set()  

    # String representation of the Drink object
    def __repr__(self): 
        return f"Drink(base={self._base}, flavors={list(self._flavors)})"

    # Getter function to return the base of the drink
    def get_base(self):
        return self._base

    # Getter function to return the flavors of the drink
    def get_flavors(self):
        return list(self._flavors)

    # Getter function to return the number of flavors in the drink
    def get_num_flavors(self):
        return len(self._flavors)

    # Method to add a flavor to the drink if it is not already present
    def add_flavor(self, flavor):
        if flavor not in self._flavors:
            self._flavors.add(flavor)

    # Method to set the flavors of the drink, resetting any existing flavors
    def set_flavors(self, flavors):
        self._flavors = set(flavors) # Resetting flavors to the new set

    valid_bases = {'water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine'}
    valid_flavors = {'lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime'}

    @classmethod                     # Class method to check if a base is valid
    def is_valid_base(cls, base):
        return base in cls.valid_bases
   
    @classmethod                     # Class method to check if a flavor is valid
    def is_valid_flavor(cls, flavor):
        return flavor in cls.valid_flavors
    
  # Creating 1st drink
drink = Drink('water')  
drink.set_flavors(['lemon', 'cherry'])
drink.add_flavor('mint')

# Creating 2nd drink
drink2 = Drink('sbrite')  
drink2.set_flavors(['strawberry', 'blueberry'])
drink2.add_flavor('lime')

# Creating a third drink 
drink3 = Drink('pokeacola')  
drink3.set_flavors(['mint', 'lime'])

# Creating an order and adding drinks to it
order = Order()
order.add_item(drink)  
order.add_item(drink2)
order.add_item(drink3)

# Creating a list to hold items from the order
my_list = []
items = order.get_items()
my_list.extend(items)


print("                                 ")
print("         --ORDER RECEIPT--       ")
print("=================================")
print(order.get_receipt())  # Output: Receipt of all drink items in the order

print(f"Drinks: {order.get_items()}")  # Output: List of drink items
print(order.get_total())  # Output: Total number of items in the order
print(order.get_num_items())  # Output: 3