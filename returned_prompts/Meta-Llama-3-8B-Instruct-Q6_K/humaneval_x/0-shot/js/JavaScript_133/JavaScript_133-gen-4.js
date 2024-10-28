Here is the Python code to solve the problem:

```Python
import math
def sumSquares(lst):
    return sum(math.ceil(x)**2 for x in lst)
```

Explanation:
The `math.ceil(x)` function is used to round each number in the list to the upper int. The `**` operator is used to square each number. The `sum` function is used to calculate the sum of the squared numbers.

Example:

```Python
print(sumSquares([1,2,3]))  # Output: 14
print(sumSquares([1,4,9]))  # Output: 98
print(sumSquares([1,3,5,7]))  # Output: 84
print(sumSquares([1.4,4.2,0]))  # Output: 29
print(sumSquares([-2.4,1,1]))  # Output: 6
```


This code will pass all the given test cases.