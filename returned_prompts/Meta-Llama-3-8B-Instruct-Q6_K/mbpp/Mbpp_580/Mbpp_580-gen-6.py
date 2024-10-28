"""
You can solve this problem as follows:

```python
def extract_even(nested_tuple):
    result = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            result.append(extract_even(element))
        elif element % 2 == 0:
            result.append(element)
    return tuple(result)
```"""

This problem asks you to create a function that takes a nested mixed tuple (a tuple that can contain other tuples and non-tuple elements) as an input, and returns a new tuple that contains only the even elements from the original tuple. The even elements can be both integers and other nested mixed tuples.

The function `extract_even` does this by iterating over each element in the input tuple. If the element is a tuple, it calls itself with that tuple as the input. If the element is an integer and it's even, it adds that element to the result tuple. Finally, it returns the result tuple.

The unit test `assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)` shows that the function should return a tuple that contains only the even elements from the original tuple. It also shows that the function should handle nested tuples correctly, by recursively calling itself with nested tuples.