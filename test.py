import unittest
from customer import Customer
from item import Item
from order import Order

class TestCustomer(unittest.TestCase):
    #set up an instance of the class
    def setUp(self):
        self.c=Customer(123,'123-456-6789')
    #test the get methods
    def test_UserID(self):
        self.assertEqual(self.c.getUserID(), 123)
    def test_phonenumber(self):
        self.assertEqual(self.c.getPhoneNumber(), '123-456-6789')

class TestItem(unittest.TestCase):
    #set up an instance of the class
    def setUp(self):
        self.c=Item(123,'Green Grapes', 3.19)
    #test the get methods
    def test_ItemID(self):
        self.assertEqual(self.c.getItemID(), 123)
    def test_ItemName(self):
        self.assertEqual(self.c.getItemName(), 'Green Grapes')
    def test_Cost(self):
        self.assertEqual(self.c.getCost(), 3.19)

class TestOrder(unittest.TestCase):
    #set up an instance of the class
    def setUp(self):
        self.c=Order(123, '2021-8-12', 123, 2, 123)
    #test the get methods
    def test_OrderID(self):
        self.assertEqual(self.c.getOrderID(), 123)
    def test_OrderDate(self):
        self.assertEqual(self.c.getOrderDate(), '2021-8-12')
    def test_ItemID(self):
        self.assertEqual(self.c.getItemID(), 123)
    def test_Quantity(self):
        self.assertEqual(self.c.getQuantity(), 2)
    def test_PaymentID(self):
        self.assertEqual(self.c.getPaymentID(), 123)
