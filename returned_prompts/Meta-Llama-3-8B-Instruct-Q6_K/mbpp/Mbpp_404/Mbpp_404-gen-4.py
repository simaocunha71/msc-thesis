```
def minimum(a, b):
    if a <= b:
        return a
    else:
        return b
```
The function takes two numbers as arguments and returns the smaller one. It does this by comparing the two numbers and returning the one that is less than or equal to the other. This function passes the given unit test `assert minimum(1,2) == 1`. 

However, this function will return the wrong result if the two numbers are equal. In this case, it will return one of the numbers, not necessarily the smallest one. If you want to return the smallest number in all cases, including when the numbers are equal, you can modify the function like this:

```
def minimum(a, b):
    if a <= b:
        return a
    else:
        return b
``` 
This function will return the smallest number, and it will also return the correct result when the numbers are equal. 

Note: Python's built-in `min` function can be used to find the minimum of two or more numbers. For example, `min(1,2)` will return `1`, and `min(1,2,3)` will return `1`. However, the purpose of this problem is to write a function that does this, rather than using the built-in function. 