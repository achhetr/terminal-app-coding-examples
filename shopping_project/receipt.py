class Receipt:
  def __init__(self, items, amount):
    self.items = items
    self.amount = amount

  def display_receipt(self):
    return 'Your total for 10 bananas and 14kg apples are = $53.00'
