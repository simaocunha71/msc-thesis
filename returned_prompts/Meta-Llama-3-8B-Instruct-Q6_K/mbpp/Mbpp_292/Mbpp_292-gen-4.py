```
def find(a, b):
    return a // b
```
This function uses the floor division operator (//) in Python, which returns the quotient of the division of the two numbers, rounded down to the nearest integer. For example, if we call `find(10,3)`, it returns `3`.  The unit test `assert find(10,3) == 3` confirms this. 

Note: The floor division operator is used, not the division operator (/), because the problem statement asks for the quotient rounded down to the nearest integer. If we use the division operator (/), the result would be a floating-point number. For example, `10 / 3` would return `3.3333333333333335`, which is not an integer.  The floor division operator (`//`) returns the largest possible integer that is less than or equal to the result of the division. In this case, `10 // 3` returns `3`, which is the desired result. 