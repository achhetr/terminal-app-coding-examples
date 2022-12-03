from order import Order
from receipt import Receipt

class TestingReceipt:
  def test_receipt_format(self):
    items = {
      'bananas': 10,
      'apples': 14
    }
    amount = Order(items).total_amount()
    assert Receipt(items, amount).display_receipt() == 'Your total for 10 bananas and 14kg apples are = $53.00'
