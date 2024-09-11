Here's a Python function that finds the last digit of a given number:

```python
def last_Digit(n):
    return (n % 10)
```

To test the function, you can use the `assert` statement. Here's an example:

```python
def test_last_digit():
    assert last_Digit(123) == 3
    print("Test Passed!")

test_last_digit()
```

This will print "Test Passed!" if the function correctly returns the last digit of the given number.

Note: The `%` operator returns the remainder of the division. In this case, we use it to get the last digit of a number by taking the remainder of the division by 10.

Also note that this function will only work correctly for positive integers. For example, if you pass a negative number or a float to this function, it will return an incorrect result.

```python
def last_Digit(n):
    return (n % 10)
```

This function is very simple and can be used to find the last digit of a given number. However, it may not be suitable for all scenarios. For example, if you want to find the last digit of a complex number or a very large number, you may need to use a different approach.

Additionally, if you are working with large numbers, you may need to consider using the `mod` function instead of the `%` operator. The `mod` function is more efficient and accurate for larger numbers. Here's an example:

```python
def last_Digit(n):
    return (n % 10)
```

This function can be used to find the last digit of any number, regardless of its size.

```python
def test_last_digit_large_number():
    assert last_Digit(1234567890) == 0
    print("Test Passed!")

test_last_digit_large_number()
```

This will print "Test Passed!" if the function correctly returns the last digit of the given large number.

In general, the choice of function depends on the specific