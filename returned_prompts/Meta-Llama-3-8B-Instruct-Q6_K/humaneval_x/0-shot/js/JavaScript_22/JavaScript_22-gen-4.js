```python
def filterIntegers(values):
    return [x for x in values if isinstance(x, int)]
```
Explanation:
The function `filterIntegers` takes a list of values as input and returns a new list containing only the integers from the original list. This is achieved using a list comprehension, which iterates over the input list and includes only the elements that satisfy the condition `isinstance(x, int)`. The `isinstance` function is used to check if an object is an instance of a particular class, in this case, the `int` class. The resulting list of integers is then returned.