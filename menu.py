class MenuItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def update_item(self, old_item, new_item):
        index = self.items.index(old_item)
        self.items[index] = new_item

    def find_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def find_by_name(self, name):
        return [item for item in self.items if item.name == name]
