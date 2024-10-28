```
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
```



The function `is_product_even` takes a list of numbers as input. It initializes a variable `product` to 1, then iterates over each number in the list, multiplying the `product` by that number. Finally, it returns `True` if the `product` is even (i.e., the remainder when divided by 2 is 0), and `False` otherwise.

The unit test `assert is_product_even([1,2,3])` checks that the function returns `True` when the product of the numbers in the list is even. The test passes because the product of 1, 2, and 3 is indeed even (6). If the product were odd, the test would fail.