```
def test_three_equal(x,y,z):
    if x==y and y==z:
        return 3
    elif x==y and y!=z:
        return 2
    elif y==z and y!=x:
        return 2
    elif z==x and z!=y:
        return 2
    else:
        return 0
```

In the above code, we create a function called `test_three_equal` that takes in three integers as parameters. Inside the function, we use a series of `if` and `elif` statements to check if all three numbers are equal, if two numbers are equal, or if only one number is equal. Based on these conditions, the function returns the appropriate result.

To test the function, we can use the `assert` statement to verify if the expected result matches the actual result. In this case, we assert that when we pass in the three numbers `1, 1, 1` to the `test_three_equal` function, the result should be `3`.

By running the code, the assertion will pass if the function correctly counts the number of equal numbers, and fail otherwise.

```python
def test_three_equal(x,y,z):
    if x==y and y==z:
        return 3
    elif x==y and y!=z:
        return 2
    elif y==z and y!=x:
        return 2
    elif z==x and z!=y:
        return 2
    else:
        return 0

assert test_three_equal(1,1,1) == 3
```

The above code will output `True` if the assertion passes, indicating that the function correctly counts the number of equal numbers.

```python
True
```

If the assertion fails, an `AssertionError` will be raised, indicating that there is an error in the function.

```python
AssertionError
```

By using this approach, you can easily test the functionality of the `test_three_equal` function and ensure that it correctly counts the number of equal numbers from the three given integers.

```python
def test_three_equal(x