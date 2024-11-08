class Payment:
    def __init__(self, order):
        self.order = order
        self.is_paid = False

    def process_payment(self, payment_method):
        self.is_paid = True
        print("Payment of " + str(self.order.total_amount) + " processed using " + payment_method)
