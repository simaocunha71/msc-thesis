```
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
```
The function `is_product_even` takes a list of numbers as input, calculates the product of all numbers in the list, and returns `True` if the product is even and `False` if the product is odd. The `assert` statement checks if the function correctly identifies the product of the list `[1,2,3]` as even. 

The function works by initializing a variable `product` to 1 and then multiplying it by each number in the list. Finally, it checks if the product is even by using the modulo operator (`%`) and returns `True` if the remainder is 0 (i.e., the product is even), and `False` otherwise. 

For example, if the input list is `[1, 2, 3]`, the function will calculate the product as `1 * 2 * 3 = 6`, which is even, so the function will return `True`. If the input list is `[1, 3, 5]`, the function will calculate the product as `1 * 3 * 5 = 15`, which is odd, so the function will return `False`. 

This function assumes that the input list is not empty. If the input list is empty, the function will return `True` because the product of no numbers is considered even. If you want to handle the case of an empty input list differently, you can add a check at the beginning of the function. For example, you can return `False` if the input list is empty, because the product of no numbers is considered odd. 