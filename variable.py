class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_saved = price - deal_price
    
    def display_product_details(self):
        print("product: {}" .format(self.name))
        print("price: {}" .format(self.price))
        print("deal_price: {}" .format(self.deal_price))
        print("ratings: {}" .format(self.ratings))
        print("you_saved: {}" .format(self.you_saved))
         
class Electronic(Product):
    def __init__(self, name, price, deal_price, ratings, warrenty):
        super().__init__(name, price, deal_price, ratings)
        self.warrenty = warrenty
    def display_product_details(self):
        super().display_product_details()
        print("warrenty: {}" .format(self.warrenty))
        
class Groccery(Product):
    def __init__(self, name, price, Deal_price, ratings, expiry_date):
        super().__init__(name, price, Deal_price, ratings)
        self.expiry_date = expiry_date
    def display_product_details(self):
        super().display_product_details()
        print("expiry_date: {}" .format(self.expiry_date))

class Order:
    delivery_charges = {
        "normal" : 0,
        "primium" : 100 
    }
    def __init__(self, delivryMethid, Address):
        self.items_in_cart = []
        self.delivryMethid = delivryMethid
        self.Address = Address
    def add_item(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)
    def disply_order_details(self):
        print("delivryMethid: {}" .format(self.delivryMethid))
        print("Address: {}" .format(self.Address)) 
        print("products")
        print("---------------------------------------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}" .format(quantity))
            print(" ")
    
Tv = Electronic("Tv", 15000, 10000, 4.1, 12)
banana = Groccery("Banana", 15, 10, 4.1, 2024)

my_order = Order("normal", "hyd")
my_order.add_item(Tv, 1)
my_order.add_item(banana, 5)
my_order.disply_order_details()












