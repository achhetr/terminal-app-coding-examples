class FruitItem:
  def __init__(self, name, unit, num, price):
    self.name = name # name of the fruit
    self.unit = unit # piece or KG
    self.price = price # $1/kg or $1/piece
    self.num = num # 10 bananas or 14 kg of apples

  def amount(self):
    return self.price * self.num

  def __str__(self):
    return f'{self.num} {self.unit} {self.name}'


# banana = FruitItem('banana', 'piece', 10, 1)
# apple = FruitItem('apple', 'kg', 14, 4)
