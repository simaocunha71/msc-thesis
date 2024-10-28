```
def find(a, b):
    return a // b
```
The function `find(a, b)` returns the quotient of `a` and `b` rounded down to the nearest integer. This is achieved by using the floor division operator `//` in python. For example, `10 // 3` returns `3`. 

The unit test `assert find(10,3) == 3` ensures that the function works correctly. If the function does not return `3` when given the input `(10,3)`, the test will fail. 

Note: The floor division operator `//` is used to divide two numbers and return the quotient rounded down to the nearest integer. It is different from the true division operator `/` which returns the quotient as a floating point number. For example, `10 / 3` returns `3.3333333333333335`, while `10 // 3` returns `3`. 