import json
PRICING_FILE_NAME = "product_pricing.json"

class Cart:
    
    
    def __init__(self, product):
  
    def add_to_cart(self, product):
        self.product.append(product)
    

    def sort_items(self):
        self.product.sort()
    
    def get_price(self, product):
        return self.pricing_file[product]