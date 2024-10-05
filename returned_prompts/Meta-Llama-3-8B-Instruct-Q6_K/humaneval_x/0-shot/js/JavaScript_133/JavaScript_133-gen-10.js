Here is a Python function that will solve this problem:

```Python
import math

def sumSquares(lst):
    return sum(math.ceil(i) ** 2 for i in lst)
```

This function uses a generator expression to calculate the square of each number in the list, round each number to the upper int using the `math.ceil` function, and then sum these results. The `math.ceil` function is used to round each number to the upper int.

Here is how you can use this function with the given examples:

```Python
print(sumSquares([1,2,3]))  # Output: 14
print(sumSquares([1,4,9]))  # Output: 98
print(sumSquares([1,3,5,7]))  # Output: 84
print(sumSquares([1.4,4.2,0]))  # Output: 29
print(sumSquares([-2.4,1,1]))  # Output: 6
```



Note: In Python, the `**` operator is used for exponentiation. For example, `a ** 2` means `a` squared. The `math.ceil` function is used to round a number up to the nearest integer. For example, `math.ceil(1.4)` would return `2`. The `sum` function is used to calculate the sum of a list of numbers. In this case, it is used to calculate the sum of the squares of the numbers in the list after rounding them up to the nearest integer.