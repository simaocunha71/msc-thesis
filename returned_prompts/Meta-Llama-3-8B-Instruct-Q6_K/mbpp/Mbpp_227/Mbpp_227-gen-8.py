```
def min_of_three(a, b, c):
    return min(a, b, c)
```
This function takes three numbers as input and returns the smallest one. The `min` function in Python returns the smallest item in an iterable or the smallest of two or more arguments. 

The unit test `assert min_of_three(10,20,0)==0` ensures that the function returns the correct result when given three different numbers. 

This function assumes that the input is a valid number. It does not handle cases where the input is not a number. In a real-world application, you might want to add error checking code to handle such cases. 