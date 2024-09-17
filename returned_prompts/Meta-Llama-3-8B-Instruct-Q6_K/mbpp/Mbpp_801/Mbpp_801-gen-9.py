```
def three_equal(a, b, c):
    return a == b == c
```


The function `three_equal(a, b, c)` takes three integers as input and returns a boolean value indicating whether all three numbers are equal. 

However, the problem statement asks for the count of equal numbers, not a boolean value. So, we need to count the number of equal numbers. 

Here's the modified function:

```
def three_equal(a, b, c):
    return 3 if a == b == c else 0
```

This function returns 3 if all three numbers are equal, and 0 otherwise. The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function works correctly when all three numbers are equal. 

If you want to count the number of equal numbers even if they are not all equal, you can modify the function as follows:

```
def three_equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b:
        return 2
    elif a == c:
        return 2
    elif b == c:
        return 2
    else:
        return 0
```

This function returns the count of equal numbers based on the number of equal pairs. For example, if two numbers are equal and one is different, it returns 2. If all three numbers are different, it returns 0.  The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function works correctly when all three numbers are equal.  The unit test `assert test_three_equal(1,1,2) == 2` ensures that the function works correctly when two numbers are equal.  The unit test `assert test_three_equal(1,2,3) == 0` ensures that the function works correctly when all three numbers are different.  