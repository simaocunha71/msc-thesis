```
def three_equal(a, b, c):
    if a == b and b == c:
        return 3
    else:
        return 0
```


This function takes three integers as input and returns the number of equal numbers. If all three numbers are equal, it returns 3; otherwise, it returns 0. The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function works correctly when all three numbers are equal. The unit test `assert three_equal(1,2,3) == 0` ensures that the function works correctly when no two numbers are equal.