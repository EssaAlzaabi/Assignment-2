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
