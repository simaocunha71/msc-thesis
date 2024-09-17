```
def find(a, b):
    return a // b
```
The problem is asking to write a function that finds the quotient of two numbers, rounded down to the nearest integer. 

The unit test `assert find(10,3) == 3` suggests that the function should return the integer part of the division. 

In Python, the `//` operator performs integer division, which discards the fractional part and returns the integer part. This is equivalent to the `math.floor` function, but more efficient.

So, the solution is a simple function that takes two arguments `a` and `b`, and returns their quotient using the `//` operator. 

This function passes the given unit test. 

Here is the test:
```
assert find(10,3) == 3
```  This test checks if the function `find(10,3)` returns `3`, which is the expected result. 

Note: This function will not work correctly if `b` is zero, as division by zero is undefined. In a real-world application, you would want to add error checking to handle this case.  For simplicity, we will ignore this case here.  If you want to handle this case, you can add a check at the beginning of the function: `if b == 0: return None or some other error handling`.  However, for this problem, we will assume that `b` will always be non-zero. 