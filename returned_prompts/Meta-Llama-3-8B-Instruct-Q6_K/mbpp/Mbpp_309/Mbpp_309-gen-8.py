```
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
```


Explanation:
This function takes two numbers as input and returns the maximum of the two. It does this by comparing the two numbers and returning the larger one. If the first number is larger, it returns the first number. If the second number is larger, it returns the second number. The function is designed to be used with any two numbers, so it can handle different types of inputs.

The unit test `assert maximum(5,10) == 10` ensures that the function works correctly. It checks that the function returns the maximum of the two numbers, which in this case is 10. If the function is working correctly, this test will pass. If the function is not working correctly, this test will fail and indicate that there is a problem with the function.