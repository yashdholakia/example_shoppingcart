# Supermarket Checkout System

This project implements a supermarket checkout system where items can be added to a cart, and the total cost of the cart can be calculated upon checkout.

## Features

- Add items to a cart
- Calculate total cost at checkout
- Support for multiple items with different prices
- Includes a suite of tests to verify functionality

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/supermarket-checkout.git
    cd supermarket-checkout
    ```

2. Install necessary dependencies (if any):
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. To run the tests, you can use `pytest`. Install `pytest` if you haven't already:
    ```sh
    pip install pytest
    ```

2. Run the tests:
    ```sh
    pytest
    ```

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

# Add more tests as needed
