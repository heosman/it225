from item import Item

class Order():
    def __init__(self, orderid, orderdate, itemid, quantity, paymentid):
        self.orderid=orderid
        self.orderdate=orderdate
        self.itemid=itemid
        self.quantity=quantity
        self.paymentid=paymentid

    def getOrderID(self):
        return self.orderid
    
    def getOrderDate(self):
        return self.orderdate
    
    def getItemID(self):
        return self.itemid

    def getQuantity(self):
        return self.quantity

    def getPaymentID(self):
        return self.paymentid

    def __str__(self):
        return self.orderid + ' ' + self.orderdate + ' ' + self.itemid + ' ' + self.quantity + ' ' + self.paymentid