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
