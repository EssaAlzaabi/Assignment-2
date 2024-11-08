class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_amount = 0.0

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()

    def remove_item(self, item):
        self.items.remove(item)
        self.calculate_total()

    def update_quantity(self, item, quantity):
        item.quantity = quantity
        item.total_price = item.ebook.price * quantity
        self.calculate_total()

    def calculate_total(self):
        self.total_amount = sum(item.total_price for item in self.items)
