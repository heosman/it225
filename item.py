class Item():
    def __init__(self, itemid, itemname, cost):
        self.itemid=itemid
        self.itemname=itemname
        self.cost=cost

    def getItemID(self):
        return self.itemid

    def getItemName(self):
        return self.itemname

    def getCost(self):
        return self.cost
