class Receipt:
  def __init__(self, order):
    self.order = order

  def display_receipt(self):
    return f'Your total for {self.order.display_list_of_items()} are = ${self.order.total_amount()}'


# order = Order()
# order.add(banana)
# order.add(apple)
# order.total_amount -> $53

# receipt = Receipt(order).display_receipt
# 'Your total for 10 bananas and 14kg apples are = $53.00'
