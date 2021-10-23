class Cart:

    def __init__(self):
        """Initialize the cart"""
        self.order = []

    def total(self) -> int:
        """Calculate the total amount of products price in the cart"""
        t = sum([p['price'] for p in self.order])
        return t

    def clean(self):
        """Remove all items from the cart"""
        self.order = []

    def add_product(self, product):
        """Add product"""
        self.order.append(product)
