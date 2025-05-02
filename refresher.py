# refresher.py
class Drink:  # Drink class to represent a drink with size, base, and flavors
    def __init__(self, size, base, flavors=None):  # Constructor to initialize the drink with size, base, and optional flavors
        valid_sizes = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'Mega': 2.15}
        valid_bases = {'water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine'}
        valid_flavors = {'lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime'}

        if size not in valid_sizes:
            raise ValueError(f"Invalid size '{size}'. Valid sizes are: {list(valid_sizes.keys())}")
        
        if base not in valid_bases:
            raise ValueError(f"Invalid base '{base}'. Valid bases are: {valid_bases}")
        
        if flavors and not all(flavor in valid_flavors for flavor in flavors):
            raise ValueError(f"Invalid flavors '{flavors}'. Valid flavors are: {valid_flavors}")

        self._size = size
        self._base = base
        self._flavors = set(flavors) if flavors else set()

    @classmethod                     # Class method to check if a base is valid
    def is_valid_base(cls, base):
        valid_bases = {'water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine'}
        return base in valid_bases
   
    @classmethod                     # Class method to check if a flavor is valid
    def is_valid_flavor(cls, flavor):
        valid_flavors = {'lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime'}
        return flavor in valid_flavors

    def get_size(self):
        return self._size if hasattr(self, '_size') else None
    
    def get_base(self):
        return self._base if hasattr(self, '_base') else None
    
    def get_flavors(self):
        return list(self._flavors) if hasattr(self, '_flavors') else []
    
    def get_num_flavors(self):
        return len(self._flavors) if hasattr(self, '_flavors') else 0
    
    def add_flavor(self, flavor):
        if flavor not in self._flavors:
            self._flavors.add(flavor)
            
    def set_flavors(self, flavors):
        self._flavors = set(flavors) if flavors else set()
        
    
    def get_price(self):
        size_price = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'Mega': 2.15}
        return size_price[self._size]
   
    def __repr__(self):
        return f"Drink(size = {self._size}, base = {self._base}, flavors = {list(self._flavors)})"
    
class Order:  # Order class to manage a collection of Drink items
    def __init__(self):
        self._items = []  # Initialize _items as an empty list

    def add_item(self, item: int):
   
        if isinstance(item, (Drink)):
            self._items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]

    def get_items(self):
        return self._items

    def get_num_items(self):
        return len(self._items)

    def get_tax(self):
        return sum(drink.get_price() * 0.075 for drink in self._items)  # Corrected tax calculation
        
    def get_total_price(self):
        return sum(drink.get_price() for drink in self._items) + self.get_tax()  # Total price including tax
    
    def get_receipt(self):
        receipt = []
        for item in self._items:
            
            if isinstance(item, Drink):
                drink = item
                receipt.append(f"Drink: {drink.get_base()}")
                receipt.append(f"Size: {drink.get_size()}, Base: {drink.get_base()}, Flavors: {', '.join(drink.get_flavors())}")
                receipt.append(f"Price: ${drink.get_price():.2f}")
                
            elif isinstance(item, Food):
                receipt.append(f"Food: {item.get_name()}, Base Price: ${item._base_price:.2f}")
                if item.get_toppings():
                    receipt.append(f"Toppings: {', '.join(item.get_toppings())}")
                    receipt.append(f"Toppings Price: ${sum(item._valid_toppings[t] for t in item.get_toppings()):.2f}")
                receipt.append(f"Total Food Price: ${item.get_price():.2f}")
                
            else:
                continue
    
        receipt.append(f"Tax: ${self.get_tax():.2f}")
        receipt.append(f"Total with Tax: ${self.get_total_price():.2f}")
        
        return (
            "\n".join(receipt) + "\n" +
            "---------------------------------\n" +
            ("Thanks for shopping with us!" if self._items else "Oops looking as empty as your stomach. Try ordering again! \n")
        )

    def __repr__(self):
        return f"Order(items={self._items})"

if __name__ == "__main__":  
    # Define the drink object
   # drink = Drink('medium', 'water', ['lemon', 'cherry'])
    drink3 = Drink('small', 'water', ['lemon', 'cherry'])
    # Create an Order object
    Order1 = Order()
    


    # Add the drink to the order
    Order1.add_item(drink3)
    
    print(Order1.get_receipt())  # Print the receipt for the order