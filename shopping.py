from supermarket import SuperMarket
import sys

products = sys.argv[1]
supermarket = SuperMarket()
cart_contents = supermarket.add_to_cart(products)
if len(cart_contents)> 0:
    total = supermarket.checkout(cart_contents)
    print(total)
else:
    print("no products to checkout")