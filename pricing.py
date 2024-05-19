import json
DISCOUNT_FILE_NAME = "discount_offers.json"
PRICING_FILE_NAME = "product_pricing.json"
class Pricing:
    
    
    def __init__(self):
        with open(DISCOUNT_FILE_NAME) as json_file:
            self.discount_offers = json.load(json_file)
        with open(PRICING_FILE_NAME) as json_file:
            self.pricing_file = json.load(json_file)
       
    def get_actual_price(self, product):
        return self.pricing_file[product]

    def check_if_product_exist(self, product):
        # print(self.pricing_file.keys())
        return product in self.pricing_file.keys()

    def calculate_discount(self, product, qty):
        if product in self.discount_offers.keys():
            discounted_qty = self.discount_offers[product]["qty"]
            discounted_price = self.discount_offers[product]["discounted_price"]

            # print(product , qty)
            if qty < discounted_qty:
                return (0,qty)
            elif qty == discounted_price:
                return (discounted_price, 0)
            else:
                if qty % discounted_qty == 0:
                    div_diff = qty / discounted_qty
                    return (div_diff * discounted_price, 0)
                else:
                    rem = qty % discounted_qty
                    discountable_qty = qty - rem
                    div_diff =  discountable_qty / discounted_qty
                    return (div_diff * discounted_price, rem)
        else:
            # print("no discount available...")
            return(0,qty)
        


