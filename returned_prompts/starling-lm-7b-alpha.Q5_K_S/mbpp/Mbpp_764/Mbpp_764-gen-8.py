"""
def number_ctr(s):
    return sum(1 for c in s if c.isdigit())


def test_number_ctr():
    assert number_ctr('program2bedone') == 1


test_number_ctr()
"""

def number_ctr(s):
    return sum(1 for c in s if c.isdigit())

def test_number_ctr():
    assert number_ctr('program2bedone') == 1

test_number_ctr()





"""
"""
In this function, `number_ctr`, we take in a string, `s`. We use a list comprehension and the `isdigit()` method to filter out all the characters in the string that are digits, and then sum up the number of filtered characters. We return the result.

In the `test_number_ctr` function, we call `number_ctr` with the string `'program2bedone'`. We expect the result to be `1`, since there is only one digit in the string. We use the `assert` statement to check if the result matches our expectation. If it doesn't, an `AssertionError` will be raised.

Finally, we call `test_number_ctr` to run the test. If the test passes, no error will be raised. If it fails, an `AssertionError` will be raised and the program will terminate.
"""
```

```python

```

```python

```
```