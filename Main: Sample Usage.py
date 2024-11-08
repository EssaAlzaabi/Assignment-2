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
