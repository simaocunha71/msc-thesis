```
import math

def multiply_num(lst):
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)
```


The problem asks you to create a function that multiplies all the numbers in a list and then divides the result by the length of the list. The function should return the result.

The unit test provided, `assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)`, suggests that the function should return the exact result, but due to floating point precision, we should use the `math.isclose` function to check if the result is close to the expected value.

Here is the solution:
```
import math

def multiply_num(lst):
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)
```
This function initializes a variable `product` to 1, then iterates over each number in the list, multiplying `product` by each number. Finally, it returns the result of dividing `product` by the length of the list. This result is then checked using the `math.isclose` function in the unit test.