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

# User Account Management: Manages customer accounts and their order history
class UserAccount:
    def __init__(self, customer):
        self.customer = customer
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def display_order_history(self):
        print("Order History for " + self.customer.name + ":")
        for order in self.order_history:
            print("- Order on " + order.order_date + " with total: " + str(order.total_amount))

# Shopping Cart Item: Represents an item in the shopping cart, including quantity and total price
class OrderItem:
    def __init__(self, ebook, quantity):
        self.ebook = ebook
        self.quantity = quantity
        self.total_price = ebook.price * quantity

# Shopping Cart: Manages items in the cart and calculates the total amount
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

# Discount Policy: Manages discount calculations based on customer loyalty and bulk purchases
class DiscountPolicy:
    def apply_discounts(self, order):
        if order.customer.loyalty_status:
            order.total_amount *= 0.9  # 10% discount for loyal customers
        if len(order.order_items) >= 5:
            order.total_amount *= 0.8  # 20% discount for bulk purchases (5 or more items)

# Payment Processing: Handles payment logic for an order
class Payment:
    def __init__(self, order):
        self.order = order
        self.is_paid = False

    def process_payment(self, payment_method):
        self.is_paid = True
        print("Payment of " + str(self.order.total_amount) + " processed using " + payment_method)

# Order Management: Processes orders, applies VAT, calculates total, and generates invoices
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
    # Catalog of available e-books with personalized titles
    ebook1 = EBook("Atomic Habits", "James Clear", "2018", "Self-help", 20.99, "ISBN987")
    ebook2 = EBook("The Lean Startup", "Eric Ries", "2011", "Business", 30.00, "ISBN654")
    ebook3 = EBook("Deep Work", "Cal Newport", "2016", "Productivity", 25.50, "ISBN321")

    # Customer account creation with a custom name
    customer1 = Customer("Ahmed Khalifa", "ahmed@example.com", "987-654-3210", True)
    user_account = UserAccount(customer1)

    # Shopping Cart operations: Adding items to cart, updating, and calculating total
    cart = ShoppingCart()
    cart.add_item(OrderItem(ebook1, 1))
    cart.add_item(OrderItem(ebook2, 1))
    cart.add_item(OrderItem(ebook3, 2))

    # Order processing: Creating an order from cart items
    order = Order(customer1, "2024-11-08")
    for item in cart.items:
        order.add_item(item)

    # Applying discounts and generating invoice
    discount_policy = DiscountPolicy()
    discount_policy.apply_discounts(order)
    order.generate_invoice()

    # Adding order to user account history and processing payment
    user_account.add_order(order)
    payment = Payment(order)
    payment.process_payment("Credit Card")

    # Displaying order history for the customer
    user_account.display_order_history()

if __name__ == "__main__":
    main()
