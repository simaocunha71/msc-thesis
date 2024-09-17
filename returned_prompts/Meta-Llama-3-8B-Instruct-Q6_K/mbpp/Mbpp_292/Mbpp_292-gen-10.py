```
def find(a, b):
    return a // b
```
Explanation:
The problem is asking to write a function that finds the quotient of two numbers. The quotient is the result of the division operation. In Python, the floor division operator is `//`. This operator returns the largest possible integer less than or equal to the division result.

The unit test `assert find(10,3) == 3` suggests that the function should return the quotient rounded down to the nearest integer. This is achieved using the floor division operator `//`.

For example, `find(10,3)` would return `3` because `10 // 3` is `3`. Similarly, `find(7,2)` would return `3` because `7 // 2` is `3`. 

The function `find(a, b)` takes two arguments `a` and `b` and returns the quotient of `a` divided by `b`. The `//` operator is used to perform the floor division. This means that any fractional part of the result is discarded, resulting in an integer quotient. 