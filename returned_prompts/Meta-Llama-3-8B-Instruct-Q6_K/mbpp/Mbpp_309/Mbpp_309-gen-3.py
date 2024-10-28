```
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
```


Explanation: 
This function takes two numbers as input and returns the maximum of the two. It uses a simple if-else statement to check if the first number is greater than the second number. If it is, then the function returns the first number. Otherwise, it returns the second number.

The unit test `assert maximum(5,10) == 10` ensures that the function is working correctly by checking if the maximum of 5 and 10 is indeed 10. This test will fail if the function is implemented incorrectly. 

This function does not use built-in functions like `max()` or `math.max()`, as per the problem description. It also does not handle the case where the input is not a number, as it is assumed that the input will always be a number. In a real-world scenario, you would want to add error handling to deal with invalid input. 