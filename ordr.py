

class Product:
  def __init__(self, name, price, deal_price, ratings):
    self.name = name
    self.price = price
    self.deal_price = deal_price
    self.ratings = ratings

  def get_deal_price(self):
    return self.deal_price
  
  def display_product_details(self):
    print("{}: {}".format(self.name, self.price))

class grocery_item(Product):
  pass

class ElectronicItem(Product):
  def __init__(self, name, price, deal_price, ratings, warranty):
    super().__init__(name, price, deal_price, ratings)
    self.warranty = warranty
  
  def display_product_details(self):
    super().display_product_details()
    print(f"Warranty: {self.warranty}")

class Order:
  def __init__(self, delivery_method, Address):
    self.items = []
    self.delivery_method = delivery_method
    self.Address = Address
  
  def Add_item(self, product, quantity):
    self.items.append((product, quantity))

  def display_order_details(self):
    for product, Quantity in self.items:
      product.display_product_details()
      print("Quantity: {}" .format(Quantity)) 
  
  def display_Toatal_Bill(self):
    total_bill = 0
    for Product, Quantity in self.items:
      price = Product.get_deal_price * Quantity
      total_bill += price
    print("Toatal_Bill: {}" .format(total_bill))


tv = ElectronicItem("Tv", 45000, 40000, 4.0, 12)
order = Order("Normal", "Hyd")
order.Add_item(tv, 1)
order.display_order_details()
