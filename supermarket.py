from pricing import Pricing # type: ignore
from collections import Counter
import sys

class SuperMarket:
    def __init__(self):
        self.pricing = Pricing()


    def add_to_cart(self, products):
        items =  Counter(list(products))
        for item in items:
            if not self.pricing.check_if_product_exist(item):
                items[item] = 0
        # print("final items : :", items)
        return items

    def checkout(self, cart_collection):
        
        

        updated_cart_collection = Counter(dict(filter(lambda x: x[1] != 0, cart_collection.items())))
        # print("updated_cart_collection", updated_cart_collection)

        final_total = 0
        for elem in updated_cart_collection:
            discount_tuple = self.pricing.calculate_discount(elem,updated_cart_collection[elem])
          
            undiscounted_price = discount_tuple[1] * self.pricing.get_actual_price(elem)
            # print("undiscounted_price", undiscounted_price)
            discounted_price = discount_tuple[0]
            # print("discounted_price",discounted_price)
            final_total+= undiscounted_price + discounted_price
        
        return int(final_total)


