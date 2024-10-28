```
def unique_product(nums):
    return math.prod(set(nums))
```



The problem is asking to write a function that calculates the product of unique numbers in a given list. 

The unit test `assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000` helps to understand the problem better. 

The solution uses the built-in `set` function to remove duplicates from the list and the `math.prod` function to calculate the product of the unique numbers. 

Here is the Python function that solves the problem:
```
def unique_product(nums):
    return math.prod(set(nums))
```



In this function, `set(nums)` is used to remove duplicates from the list, and `math.prod(set(nums))` is used to calculate the product of the unique numbers. The `math.prod` function is available in Python 3.8 and later. For earlier versions of Python, you can use the `functools.reduce` function with the `operator.mul` function to calculate the product:
```
import functools
import operator

def unique_product(nums):
    return functools.reduce(operator.mul, set(nums), 1)
```



This function works by initializing the product to 1, then iterating over the unique numbers in the list and multiplying the product by each number. The `functools.reduce` function applies a binary function (in this case, multiplication) to all items in an iterable, so as to reduce the iterable to a single output. The `operator.mul` function is a function object that implements multiplication. The `set(nums)` is used to remove duplicates from the list. The `1` is the initial value of the product. 