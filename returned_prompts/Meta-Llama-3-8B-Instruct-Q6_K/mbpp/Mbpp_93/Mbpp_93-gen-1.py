```
def power(a, b):
    return a ** b
```


The problem is asking to create a function that calculates the value of 'a' to the power 'b'. 

However, the problem description does not specify the type of 'a' and 'b'. They could be integers, floats, or even complex numbers. 

Luckily, the unit test provided gives us a hint about the expected behavior of the function. The test `assert power(3,4) == 81` suggests that the function should work with integers. 

Based on this, we can write a simple function that uses the built-in exponentiation operator (`**`) in Python. This operator can be used with integers and returns the result of the exponentiation.

Here is the solution:
```
def power(a, b):
    return a ** b
```


This function takes two arguments 'a' and 'b', and returns the result of 'a' raised to the power 'b'. The `**` operator is used to perform the exponentiation. 

For example, if you call `power(3, 4)`, the function will return `3 ** 4`, which is equal to `81`. 

This function should pass the provided unit test. However, please note that this function does not handle non-integer values of 'a' and 'b'. If you want to handle non-integer values, you would need to use a more complex implementation, such as using a loop or recursion. 