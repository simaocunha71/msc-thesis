```
def power(a, b):
    return a ** b
```


The problem is asking for a function that calculates the value of 'a' to the power 'b'. 

The unit test provided, `assert power(3,4) == 81`, suggests that the function should return the result of 'a' raised to the power 'b'. 

The `**` operator in Python is used for exponentiation, so we can use this operator to write the function. 

Here is the solution:

```
def power(a, b):
    return a ** b
```


This function takes two arguments, 'a' and 'b', and returns the result of 'a' raised to the power 'b'. 

For example, `power(3,4)` would return `3 ** 4`, which is `81`. 

The unit test `assert power(3,4) == 81` would pass with this function. 

This function works for positive integer values of 'a' and 'b', but it would need to be modified to handle negative numbers, non-integer values, or complex numbers.  However, based on the provided unit test, this function is sufficient. 