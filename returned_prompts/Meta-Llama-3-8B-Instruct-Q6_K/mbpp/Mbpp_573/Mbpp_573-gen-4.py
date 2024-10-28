```
def unique_product(lst):
    return prod(set(lst))

import math
def prod(iterable):
    result = 1
    for value in iterable:
        result *= value
    return result
```


Explanation:
The problem asks to write a function that calculates the product of the unique numbers in a given list. 

The function `unique_product` takes a list of numbers as an argument. It first converts the list into a set, which removes duplicates. Then it calls another function `prod` with this set as an argument. The `prod` function calculates the product of all numbers in the set.

The unit test `assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000` ensures that the function works correctly.

The `prod` function is a recursive function that takes an iterable as an argument. It initializes a variable `result` to 1, then iterates over each value in the iterable. For each value, it multiplies `result` by the value. Finally, it returns `result`. This function is used to calculate the product of all numbers in the set. 

The `unique_product` function is a simple function that calls `prod` with a set of unique numbers. It is used to calculate the product of the unique numbers in a given list. 












