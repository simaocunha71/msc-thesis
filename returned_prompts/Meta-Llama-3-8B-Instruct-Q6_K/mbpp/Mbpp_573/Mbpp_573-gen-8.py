```
def unique_product(lst):
    return math.prod(set(lst))
```
This function works by first converting the list to a set, which removes any duplicate numbers. It then uses the `math.prod` function to calculate the product of the numbers in the set. The `math.prod` function was added in Python 3.8, if you are using an earlier version, you can use the `functools.reduce` function with the `operator.mul` function instead:
```
import functools
import operator

def unique_product(lst):
    return functools.reduce(operator.mul, set(lst), 1)
```
The unit test `assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000` suggests that the product of the unique numbers in the list is 720000000, which is the product of the numbers 10, 20, 30, 40, 50, and 60. The function correctly calculates this product. 