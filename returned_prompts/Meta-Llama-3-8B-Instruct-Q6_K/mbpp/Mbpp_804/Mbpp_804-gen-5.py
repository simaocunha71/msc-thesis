```
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
``` 
This function calculates the product of all numbers in the list and checks if the result is even by using the modulus operator `%`. If the remainder of the product divided by 2 is 0, then the product is even. 

The unit test `assert is_product_even([1,2,3])` ensures that the function works correctly for a list of numbers. 

This function does not handle the case where the input list is empty. Depending on the requirements, you might want to add a check for this case and return a specific value (e.g., `True` or `False`) or raise an exception. 

For example:
```
def is_product_even(lst):
    if not lst:
        return True  # or raise ValueError("List is empty")
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
``` 