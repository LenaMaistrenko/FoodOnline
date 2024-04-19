class Order:
    def __init__(self):
        self.items = []
        self.status = "Pending"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def place_order(self):
        if self.status == "Pending":
            self.status = "Placed"
        else:
            print("Order has already been placed.")

    def cancel_order(self):
        if self.status == "Placed":
            self.status = "Cancelled"
            print("Order has been cancelled.")
        else:
            print("Order cannot be cancelled.")

    def track_order_status(self):
        return self.status
