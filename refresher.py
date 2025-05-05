# refresher.py
class Drink:
    """
    Represents a customizable drink with a specific size, base, and optional flavors.

    Attributes:
        _size (str): Size of the drink (e.g., small, medium, large, Mega).
        _base (str): The base liquid used in the drink (e.g., water, pokeacola).
        _flavors (set): A set of added flavors (e.g., lemon, mint).

    Methods:
        get_size(): Returns the drink size.
        get_base(): Returns the drink base.
        get_flavors(): Returns a list of added flavors.
        get_num_flavors(): Returns the count of added flavors.
        add_flavor(flavor): Adds a flavor if it's not already present.
        set_flavors(flavors): Sets the entire list of flavors.
        get_price(): Returns the base price based on size.
        __repr__(): Returns a string representation of the drink.
    """
    def __init__(self, size, base, flavors=None):
        """Initializes a Drink with size, base, and optional flavors."""
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

    @classmethod
    def is_valid_base(cls, base):
        """Checks if the provided base is valid."""
        valid_bases = {'water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine'}
        return base in valid_bases

    @classmethod
    def is_valid_flavor(cls, flavor):
        """Checks if the provided flavor is valid."""
        valid_flavors = {'lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime'}
        return flavor in valid_flavors

    def get_size(self):
        """Returns the size of the drink."""
        return self._size if hasattr(self, '_size') else None

    def get_base(self):
        """Returns the base of the drink."""
        return self._base if hasattr(self, '_base') else None

    def get_flavors(self):
        """Returns the list of added flavors."""
        return list(self._flavors) if hasattr(self, '_flavors') else []

    def get_num_flavors(self):
        """Returns the number of added flavors."""
        return len(self._flavors) if hasattr(self, '_flavors') else 0

    def add_flavor(self, flavor):
        """Adds a new flavor to the drink if not already present."""
        if flavor not in self._flavors:
            self._flavors.add(flavor)

    def set_flavors(self, flavors):
        """Sets a new list of flavors for the drink."""
        self._flavors = set(flavors) if flavors else set()

    def get_price(self):
        """Returns the price of the drink based on its size."""
        size_price = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'Mega': 2.15}
        return size_price[self._size]

    def __repr__(self):
        """Returns a string representation of the drink."""
        return f"Drink(size = {self._size}, base = {self._base}, flavors = {list(self._flavors)})"


class Order:
    """
    Represents a customer's order containing multiple Drink (or Food) items.

    Attributes:
        _items (list): List of Drink or Food items in the order.

    Methods:
        add_item(item): Adds a valid item to the order.
        remove_item(index): Removes an item at the specified index.
        get_items(): Returns the list of items.
        get_num_items(): Returns the number of items in the order.
        get_tax(): Calculates the total tax (7.5%).
        get_total_price(): Calculates total including tax.
        get_receipt(): Returns a printable receipt for the order.
        __repr__(): Returns a string representation of the order.
    """
    def __init__(self):
        """Initializes an empty order."""
        self._items = []

    def add_item(self, item: int):
        """Adds an item to the order if it's an instance of Drink."""
        if isinstance(item, (Drink)):
            self._items.append(item)

    def remove_item(self, index):
        """Removes an item from the order at the given index."""
        if 0 <= index < len(self._items):
            del self._items[index]

    def get_items(self):
        """Returns the list of items in the order."""
        return self._items

    def get_num_items(self):
        """Returns the number of items in the order."""
        return len(self._items)

    def get_tax(self):
        """Calculates and returns the total tax for the order (7.5%)."""
        return sum(drink.get_price() * 0.075 for drink in self._items)

    def get_total_price(self):
        """Calculates and returns the total price including tax."""
        return sum(drink.get_price() for drink in self._items) + self.get_tax()

    def get_receipt(self):
        """Generates a formatted receipt string for the order."""
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
        """Returns a string representation of the order."""
        return f"Order(items={self._items})"


if __name__ == "__main__":
    drink3 = Drink('small', 'water', ['lemon', 'cherry'])
    Order1 = Order()
    Order1.add_item(drink3)
    print(Order1.get_receipt())
