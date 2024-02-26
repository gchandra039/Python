class Order:
  def __init__(self, delivery_method, address):
    self.items = []
    self.delivery_method = delivery_method
    self.address = address

  def add_item(self, product, quantity):
    self.items.append((product, quantity))

  def display_order_details(self):
    for product, quantity in self.items:
      product.display_product_details()
      print(f"Quantity: {quantity}")

  def display_total_bill(self):
    total_bill = 0
    for product, quantity in self.items:
      price = product.get_deal_price() * quantity  # Corrected the method call
      total_bill += price
    print(f"Total_Bill: {total_bill}")

class Product:
  def __init__(self, name, price, deal_price, ratings):
    self.name = name
    self.price = price
    self.deal_price = deal_price
    self.ratings = ratings

  def get_deal_price(self):
    return self.deal_price

  def display_product_details(self):
    print(f"{self.name} - Price: {self.price}")

class GroceryItem(Product):
  pass

class ElectronicItem(Product):
  def __init__(self, name, price, deal_price, ratings, warranty):
    super().__init__(name, price, deal_price, ratings)
    self.warranty = warranty

  def get_warranty(self):
    return self.warranty

  def display_product_details(self):
    super().display_product_details()
    print(f"Warranty: {self.warranty}")

tv = ElectronicItem("TV", 45000, 40000, 4.0, 12)
order = Order("Normal", "Hyd")
order.add_item(tv, 1)
order.display_order_details()
order.display_total_bill()