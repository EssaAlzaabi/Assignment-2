class DiscountPolicy:
    def apply_discounts(self, order):
        if order.customer.loyalty_status:
            order.total_amount *= 0.9  # 10% discount for loyal customers
        if len(order.order_items) >= 5:
            order.total_amount *= 0.8  # 20% discount for bulk purchases (5 or more items)
