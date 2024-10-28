```
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
``` 

The function `is_product_even` takes a list of numbers as input, calculates the product of these numbers, and returns `True` if the product is even, and `False` otherwise. The function uses a loop to multiply all the numbers in the list together, and then checks if the result is divisible by 2 (i.e., if it's even). 

The unit test `assert is_product_even([1,2,3])` ensures that the function works correctly for the given input. 

Note: The problem statement does not specify whether the list can be empty or not. In this solution, we assume that the list cannot be empty, as it would cause a ZeroDivisionError when calculating the product. If the list can be empty, we should add a check at the beginning of the function to handle this case. For example: `if not lst: return True` (since the product of no numbers is 1, which is even). 

However, based on the unit test provided, it seems that the list cannot be empty, as it would cause a TypeError when trying to multiply the product by the first number. Therefore, we can assume that the list always contains at least one number. 

Also, the function returns `True` for an empty list, which is a reasonable assumption, as the product of no numbers is 1, which is even. However, if we want to handle the case where the list is empty, we can add a check at the beginning of the function to return `True` if the list is empty, as mentioned above. 