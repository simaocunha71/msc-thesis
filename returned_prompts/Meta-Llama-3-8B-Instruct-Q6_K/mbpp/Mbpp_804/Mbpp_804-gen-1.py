```
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
```
The function `is_product_even` takes a list of numbers as an argument, calculates the product of all numbers in the list, and returns `True` if the product is even and `False` otherwise. The unit test `assert is_product_even([1,2,3])` confirms that the function works correctly.