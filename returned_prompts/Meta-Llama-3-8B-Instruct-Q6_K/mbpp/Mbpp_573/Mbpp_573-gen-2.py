```
def unique_product(lst):
    return math.prod(set(lst))
```


The function takes a list of numbers as an argument, converts it to a set to remove duplicates, and then uses the math.prod function to calculate the product of the unique numbers in the list. The math.prod function is available in Python 3.8 and later versions.

In earlier versions of Python, you can use the functools.reduce function with the operator.mul function to achieve the same result:

```
from functools import reduce
from operator import mul

def unique_product(lst):
    return reduce(mul, set(lst), 1)
```

This function works by applying the mul function (which multiplies two numbers) to the elements of the set in order, starting with the identity element 1. The result is the product of all the unique numbers in the list.