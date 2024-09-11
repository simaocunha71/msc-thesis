Here's one way to do it:

```python
def differ_At_One_Bit_Pos(x,y):
    xx = bin(x)
    yy = bin(y)
    if len(set(xx[2:]) & set(yy[2:]))!=1:
        return False
    return True
```

Explanation:

The function `differ_At_One_Bit_Pos` takes two integer parameters `x` and `y`. It converts the integers to binary strings using the built-in `bin` function. The binary representation of a number is prefixed with `0b`, so we need to remove this prefix using slicing (`[2:]`). We then convert the binary strings to sets of characters using the built-in `set` function. This allows us to compare the unique characters in the binary strings. If the length of the intersection of the two sets is not equal to 1, it means that the two numbers differ at more than one bit position, so we return `False`. Otherwise, we return `True`.

To test the function, you can use the `assert` statement to check if the function returns the expected result for the given example:

```python
assert differ_At_One_Bit_Pos(13,9) == True
```

This will raise an `AssertionError` if the function doesn't return `True` for the example.

```python
def differ_At_One_Bit_Pos(x,y):
    xx = bin(x)
    yy = bin(y)
    if len(set(xx[2:]) & set(yy[2:]))!=1:
        return False
    return True
```

The `bin` function converts the numbers to binary strings, and the `[2:]` slicing removes the `0b` prefix. The `set` function is used to compare the unique characters in the binary strings, and the `len` function is used to check the length of the intersection of the sets. The `!=` operator is used to check if the length is not equal to 1, indicating that the numbers differ at more than one bit position. The `return False` statement returns `False` in this case, and the