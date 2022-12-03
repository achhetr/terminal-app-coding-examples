from fruit_item import FruitItem
from order import Order
from receipt import Receipt

banana = FruitItem('banana', 'piece', 10, 1)
apple = FruitItem('apple', 'kg', 14, 4)
pineapple = FruitItem('pineapple', 'piece', 12, 3)

order = Order()
order.add(banana)
order.add(apple)
order.add(pineapple)

receipt = Receipt(order)

print(receipt.display_receipt())
