class Order:
  def __init__(self):
    self.items = [] # banana, apple

  def total_amount(self):
    amount = 0
    for item in self.items:
      amount += item.amount()

    return amount

  def add(self, item):
    self.items.append(item)

  def display_list_of_items(self): #10 bananas and 14kg apples
    display = []
    for item in self.items:
      display.append(item.__str__())

    return ' and '.join(display)
    # ['a','b','c'].join(' ') => 'a b c'


# order = Order()
# order.add(banana)
# order.add(apple)
# order.total_amount -> $53
