```
def power(a, b):
    return a ** b
```
The problem is asking you to write a function that calculates the value of 'a' to the power 'b'. 

The unit test `assert power(3,4) == 81` suggests that the function should return the result of the power operation as an integer, which is the case when both 'a' and 'b' are integers and 'b' is positive.

In Python, the built-in exponentiation operator '**' can be used to calculate the power of a number. Therefore, the function can be implemented as follows:

```
def power(a, b):
    return a ** b
```


This function takes two arguments 'a' and 'b', and returns the result of 'a' to the power 'b'. The '**' operator in Python is used for exponentiation, and it returns the result as a float if 'b' is not an integer. However, since the unit test suggests that the result should be an integer, we can use the '**' operator directly without any additional checks or conversions. 