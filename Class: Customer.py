class Customer:
    def __init__(self, name, email, phone_number, loyalty_status=False):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.loyalty_status = loyalty_status
