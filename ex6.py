class Order:
  def __init__(self, delivery_method, Address):
    self.items = []
    self.delivery_method = delivery_method
    self.Address = Address
  
  def Add_item(self, product, quantity):
    self.items.append((product, quantity))

  def get_items(self):
    # return self.items
    for product, quantity in self.items:
      print(product)
  

e=Order("pr", "jdkj")
e.Add_item("lpa", 3)
e.Add_item("sd", 5) 
e.Add_item("lpa", 3)
print(e.get_items())
e.get_items()