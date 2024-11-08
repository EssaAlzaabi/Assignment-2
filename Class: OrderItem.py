class OrderItem:
    def __init__(self, ebook, quantity):
        self.ebook = ebook
        self.quantity = quantity
        self.total_price = ebook.price * quantity
