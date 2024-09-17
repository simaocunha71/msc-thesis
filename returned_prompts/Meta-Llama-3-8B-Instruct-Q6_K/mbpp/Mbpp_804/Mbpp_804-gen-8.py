```
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
```
The function `is_product_even` takes a list of numbers as input and returns `True` if the product of the numbers is even and `False` otherwise. It achieves this by initializing a variable `product` to 1, then iterating over each number in the list and multiplying it with the `product`. Finally, it checks if the `product` is even by using the modulo operator `%` and comparing the result with 0. If the result is 0, it means the product is even, otherwise it's odd. The unit test `assert is_product_even([1,2,3])` ensures the function works correctly. 





