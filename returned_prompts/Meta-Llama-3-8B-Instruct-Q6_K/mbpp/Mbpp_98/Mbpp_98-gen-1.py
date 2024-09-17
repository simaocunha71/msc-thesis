```
import math

def multiply_num(lst):
    result = 1
    for num in lst:
        result *= num
    return result / len(lst)
```


The function takes a list of numbers and multiplies all the numbers together. Then, it divides the product by the length of the list. The result is the average product of the numbers in the list.

The unit test provided ensures that the function works correctly. It checks if the result of the function is close to -67.2, which is the expected result for the given list. The `math.isclose` function is used to compare the result with the expected value with a relative tolerance of 0.001. This means that the result is considered correct if it is within 0.1% of the expected value.