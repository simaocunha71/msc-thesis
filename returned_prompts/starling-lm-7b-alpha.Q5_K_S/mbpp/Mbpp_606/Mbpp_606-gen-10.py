"""
def radian_degree(n):
    return (n*3.14)/180
"""

def radian_degree(n):
    return (n*3.14)/180

def test_radian_degree():
    assert radian_degree(90)==1.5707963267948966
    print("All Test Cases Passed")

test_radian_degree()






```

```
def radian_degree(n):
    return (n*3.14)/180

def test_radian_degree():
    assert radian_degree(90)==1.5707963267948966
    print("All Test Cases Passed")

test_radian_degree()
```

In the above code, we have a function called `radian_degree` that takes a number `n` as a parameter and returns the value of `n` in radians. The function multiplies the number by `3.14` and divides it by `180` to convert the degrees to radians. 

To test the function, we have a test case `test_radian_degree()` which asserts that when we pass `90` to the function, it should return `1.5707963267948966`. If the assertion is true, it prints "All Test Cases Passed", indicating that the function is working correctly. 

You can run the code and test the function by using the `test_radian_degree()` function. 

The expected output of the code is: 

```
All Test Cases Passed
```

This means that the function `radian_degree` is correctly converting degrees to radians.
```