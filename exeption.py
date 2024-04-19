class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds for the payment."):
        self.message = message
        super().__init__(self.message)

class MenuItemNotFoundError(Exception):
    def __init__(self, message="Menu item not found."):
        self.message = message
        super().__init__(self.message)
