"""
Here is a simple solution using python:

```python
def number_ctr(s):
    return sum(c.isdigit() for c in s)

print(number_ctr('program2bedone'))  # Outputs: 1
```

This function works by using the `isdigit` method of the string class which returns `True` if the character is a digit and `False` otherwise. The `sum` function then adds up all the `True` values, effectively counting the number of digits in the string.

Remember to use python 3 to run this code as the `isdigit` function is a built-in method of the string class in python 3.
"""

