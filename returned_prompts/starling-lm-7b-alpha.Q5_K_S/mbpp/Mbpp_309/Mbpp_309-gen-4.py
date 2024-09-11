def maximum(a,b):
    if(a>b):
        return a
    else:
        return b

# assert maximum(5,10) == 10

def test_maximum():
    assert maximum(5,10) == 10
    print('All tests passed')

test_maximum()




"""

To find the maximum of two numbers, you can write a function that compares the two numbers and returns the greater one. Here's an example implementation in Python:

```python
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
```

In this code, the function `maximum` takes two parameters, `a` and `b`, representing the two numbers to compare. It uses an `if` statement to check if `a` is greater than `b`. If it is, the function returns `a`, otherwise it returns `b`. This ensures that the function always returns the maximum of the two numbers.

To test the function, you can use the `assert` statement to check if the function returns the expected result. In the provided code, the `test_maximum` function is defined to test the `maximum` function with the values 5 and 10. The `assert` statement checks if the result of calling `maximum(5, 10)` is equal to 10, and if it is, it prints "All tests passed". If the assertion fails, an error message will be raised.

By running the `test_maximum` function, you can verify that the `maximum` function is working correctly and returning the maximum of the two input numbers.

"""





























































































































