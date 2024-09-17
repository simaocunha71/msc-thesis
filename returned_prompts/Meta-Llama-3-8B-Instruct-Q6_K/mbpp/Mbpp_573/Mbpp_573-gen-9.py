```
def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product
```
The function `unique_product` calculates the product of the unique numbers in a given list. It does this by first converting the list to a set, which removes any duplicate numbers. It then initializes a variable `product` to 1, and for each unique number in the set, it multiplies `product` by that number. Finally, it returns the calculated product.

This function passes the given unit test:
```
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
``` 