from supermarket import SuperMarket
import sys

if len(sys.argv) == 1:
    print(0)
    sys.exit(0)
products = sys.argv[1]
supermarket = SuperMarket()
cart_contents = supermarket.add_to_cart(products)
if len(cart_contents)> 0:
    total = supermarket.checkout(cart_contents)
    print(total)
else:
    print(0)