# Supermarket Checkout System

This project implements a supermarket checkout system where items can be added to a cart, and the total cost of the cart can be calculated upon checkout.

## Features

- Add items to a cart
- Calculate total cost at checkout
- Support for multiple items with different prices including discounts
- Support to modify Pricing and Discount
- Includes a suite of tests to verify functionality

## Getting Started 

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yashdholakia/example_shoppingcart.git
    
    ```

2. Install necessary dependencies (if any):
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. To run the script, you can use `shopping.py`. 
    ```python
    python shopping.py <products>
    ```
    Refer the product_pricing.json and discount_offers.json for more information

    for example, 
    ```python
    python shopping.py AB
    ```
    will produce the output of 80 (total of A and B from product_pricing.json)

    From the discount_offers.json if same products in more qty are added, it will add the discount.

    for example, 
    ```python
    python shopping.py AAABB
    ```
    will produce the output of 175 (will calculate discounted price from discount_offers.json) instead of 210

    
2. Run the tests:
    ```sh
    pytest
    ```
Note: 
 - If you add any product name which is not present in product_pricing.json (such as PQR, XYZ) it will return 0 as product does not exist.
 - If you combine both products which are present and not present, it will omit the not existing one and produce the output of existing one
    For Example, 
    ```python
    python shopping.py AB
    ```
    AND 

     ```python
    python shopping.py ABXY
    ```
    would produce same output as X and Y are not present so they will be omitted

### Example Tests

Here are some example tests included in the project:

```python
def test_example_1():
    cart_contents = supermarket.add_to_cart("")
    total = supermarket.checkout(cart_contents)
    print("'' | ", total)
    assert total == 0

def test_example_2():
    cart_contents = supermarket.add_to_cart("A")
    total = supermarket.checkout(cart_contents)
    print("A  | ", total)
    assert total == 50

def test_example_3():
    cart_contents = supermarket.add_to_cart("AB")
    total = supermarket.checkout(cart_contents)
    print("AB  | ", total)
    assert total == 80
```

### Docker Containerization
To containerize the application, follow these steps:

1. Build the Docker image:
    ```sh
    docker build -t shoppingcart .
    ```
2. Run the Docker container:

    Assuming A and B are products added to cart, put it as following command line paramter
    ```sh
         docker run shoppingcart python shopping.py AB
    ```
3. Run tests in Docker container

    ```sh
         docker run shoppingcart pytest 
    ```

For other Usecases, refer the Usage Section.

### Product Pricing files
Two JSON files are given to set product pricing and dicsount offers. Feel free to modify those! 
Note: Tests needs to be modified if these files are modified.

1. product_pricing.json
    ```json
    {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }
    ```
 Here A,B,C,D are product names and their values are prices

 2. discount_offers.json
    ```json
        {
            "A" : {
                "qty" : 3,
                "discounted_price" : 130
            },
            "B" : {
                "qty" : 2,
                "discounted_price" : 45
            }
        }
    ```