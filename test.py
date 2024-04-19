import unittest
from menu import MenuItem, Menu


class TestMenu(unittest.TestCase):
    def test_add_item_to_menu(self):
        menu = Menu()
        item = MenuItem("Burger", "Main Course", 10.99)
        menu.add_item(item)
        self.assertIn(item, menu.items)








if __name__ == '__main__':
    unittest.main()
