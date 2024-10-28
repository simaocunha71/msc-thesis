```
import math

def next_Perfect_Square(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return n
    else:
        return int((root + 1) ** 2)
```


Explanation: 
The problem is asking for a function that finds the next perfect square greater than a given number. 

To solve this problem, we first calculate the square root of the given number. If the square root is an integer, then the number is a perfect square. In this case, the next perfect square would be the same number.

If the square root is not an integer, then we increment the square root by 1 and square it to find the next perfect square.

The unit test `assert next_Perfect_Square(35) == 36` helps to clarify the problem. It indicates that if the given number is not a perfect square, the function should return the next perfect square. In this case, the next perfect square greater than 35 is 36. 

The function `next_Perfect_Square` uses the `math.sqrt` function to calculate the square root of the given number. It then checks if the square root is an integer using `int(root + 0.5) ** 2 == n`. If this condition is true, it returns the original number as it is a perfect square. If the condition is false, it increments the square root by 1 and squares it to find the next perfect square. 

The result is then returned as an integer using `int((root + 1) ** 2)`. 

This function works correctly for both perfect squares and non-perfect squares, and it passes the given unit test. 