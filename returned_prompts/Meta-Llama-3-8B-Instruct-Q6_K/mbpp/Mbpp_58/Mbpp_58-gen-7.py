```
def opposite_Signs(a, b):
    return ((a > 0) ^ (b > 0))
```





Explanation:
The function takes two integers a and b as input. It returns True if the two numbers have opposite signs and False if they have the same sign.

The expression (a > 0) ^ (b > 0) is used to check whether the two numbers have opposite signs. The ^ operator is the bitwise XOR operator in Python, which returns 1 if the two bits are different and 0 if the two bits are the same.

The expression (a > 0) returns True if a is positive and False if a is non-positive. Similarly, (b > 0) returns True if b is positive and False if b is non-positive.

So, the expression (a > 0) ^ (b > 0) returns True if a and b have opposite signs and False if they have the same sign.

The unit test `assert opposite_Signs(1,-2) == True` passes because the function correctly identifies that 1 and -2 have opposite signs.