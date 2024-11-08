# E-book Management: EBook catalog with detailed attributes
class EBook:
    def __init__(self, title, author, publication_date, genre, price, isbn):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.price = price
        self.isbn = isbn

    def __str__(self):
        return "Title: " + self.title + ", Author: " + self.author + ", Price: " + str(self.price)

# Customer Management: Customer details and loyalty status
class Customer:
    def __init__(self, name, email, phone_number, loyalty_status=False):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.loyalty_status = loyalty_status

# Shopping Cart and Orders: OrderItem to handle e-book and quantity per order
class OrderItem:
    def __init__(self, ebook, quantity):
        self.ebook = ebook
        self.quantity = quantity
        self.total_price = ebook.price * quantity

# Shopping Cart and Orders: ShoppingCart for managing cart items
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

# Order Management: Order to handle order details, VAT, discounts, and invoicing
class Order:
    def __init__(self, customer, order_date):
        self.customer = customer
        self.order_date = order_date
        self.order_items = []
        self.total_amount = 0.0
        self.vat_rate = 0.08  # 8% VAT rate

    def add_item(self, item):
        self.order_items.append(item)
        self.calculate_total()

    def calculate_total(self):
        self.total_amount = sum(item.total_price for item in self.order_items)
        self.total_amount += self.total_amount * self.vat_rate

    def apply_discounts(self):
        # Loyalty discount
        if self.customer.loyalty_status:
            self.total_amount *= 0.9  # 10% discount for loyal customers
        # Bulk purchase discount (20%) for 5 or more items
        if len(self.order_items) >= 5:
            self.total_amount *= 0.8
        # Apply VAT on the discounted total
        self.total_amount += self.total_amount * self.vat_rate

    def generate_invoice(self):
        print("Invoice for " + self.customer.name)
        print("Order Date: " + self.order_date)
        print("Items:")
        for item in self.order_items:
            print("- " + item.ebook.title + " x " + str(item.quantity) + " @ " + str(item.ebook.price) + " each")
        print("Total Amount (with VAT): " + str(round(self.total_amount, 2)))
        if self.customer.loyalty_status:
            print("Loyalty Discount Applied")
        if len(self.order_items) >= 5:
            print("Bulk Purchase Discount Applied")

# Main program logic simulating a customer session
def main():
    # Catalog of available e-books with more personalized titles
    ebook1 = EBook("Atomic Habits", "James Clear", "2018", "Self-help", 20.99, "ISBN987")
    ebook2 = EBook("The Lean Startup", "Eric Ries", "2011", "Business", 30.00, "ISBN654")
    ebook3 = EBook("Deep Work", "Cal Newport", "2016", "Productivity", 25.50, "ISBN321")

    # Customer account creation with a custom name
    customer1 = Customer("Ahmed Khalifa", "ahmed@example.com", "987-654-3210", True)

    # Shopping Cart operations: Adding items to cart, updating, and calculating total
    cart = ShoppingCart()
    cart.add_item(OrderItem(ebook1, 1))
    cart.add_item(OrderItem(ebook2, 1))
    cart.add_item(OrderItem(ebook3, 2))

    # Order processing: Creating an order from cart items
    order = Order(customer1, "2024-11-04")
    for item in cart.items:
        order.add_item(item)

    # Applying discounts and generating invoice
    order.apply_discounts()
    order.generate_invoice()  # Prints the itemized invoice with discounts and VAT

if __name__ == "__main__":
    main()