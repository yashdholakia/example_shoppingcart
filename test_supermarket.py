from supermarket import SuperMarket


supermarket = SuperMarket()

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

def test_example_4():
    cart_contents = supermarket.add_to_cart("CDBA")
    total = supermarket.checkout(cart_contents)
    print("CDBA  | ", total)
    assert total == 115

def test_example_5():
    cart_contents = supermarket.add_to_cart("AA")
    total = supermarket.checkout(cart_contents)
    print("AA | ", total)
    assert total == 100

def test_example_6():
    cart_contents = supermarket.add_to_cart("AAA")
    total = supermarket.checkout(cart_contents)
    print("AAA | ", total)
    assert total == 130

def test_example_7():
    cart_contents = supermarket.add_to_cart("AAAA")
    total = supermarket.checkout(cart_contents)
    print("AAAA | ", total)
    assert total == 180

def test_example_8():
    cart_contents = supermarket.add_to_cart("AAAAA")
    total = supermarket.checkout(cart_contents)
    print("AAAAA | ", total)
    assert total == 230

def test_example_9():
    cart_contents = supermarket.add_to_cart("AAAAAA")
    total = supermarket.checkout(cart_contents)
    print("AAAAAA | ", total)
    assert total == 260

def test_example_10():
    cart_contents = supermarket.add_to_cart("AAAB")
    total = supermarket.checkout(cart_contents)
    print("AAAB | ", total)
    assert total == 160

def test_example_11():
    cart_contents = supermarket.add_to_cart("AAABB")
    total = supermarket.checkout(cart_contents)
    print("AAABB | ", total)
    assert total == 175

def test_example_12():
    cart_contents = supermarket.add_to_cart("AAABBD")
    total = supermarket.checkout(cart_contents)
    print("AAABBD | ", total)
    assert total == 190

def test_example_13():
    cart_contents = supermarket.add_to_cart("DABABA")
    total = supermarket.checkout(cart_contents)
    print("DABABA | ", total)
    assert total == 190

def test_invalid_product():
    cart_contents = supermarket.add_to_cart("Z")
    total = supermarket.checkout(cart_contents)
    print("Z | ", total)
    assert total == 0

def test_invalid_product_with_valid_product():
    cart_contents = supermarket.add_to_cart("ABZ")
    total = supermarket.checkout(cart_contents)
    print("AB | ", total)
    assert total == 80

def test_example_test_invalid_products_with_valid_discounted():
    cart_contents = supermarket.add_to_cart("AAABBDYZ")
    total = supermarket.checkout(cart_contents)
    print("AAABBD | ", total)
    assert total == 190

def test_example_test_invalid_products_with_one_valid():
    cart_contents = supermarket.add_to_cart("PQRTUVQZYZA")
    total = supermarket.checkout(cart_contents)
    print("AAABBD | ", total)
    assert total == 50