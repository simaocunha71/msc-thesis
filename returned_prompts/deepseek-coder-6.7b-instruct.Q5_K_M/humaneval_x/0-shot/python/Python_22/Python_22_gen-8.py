from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]


print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))

This code uses list comprehension to iterate over the values in the input list. It includes a value in the output list if it is of type int, which is checked by the built-in function isinstance().
"""
</pre>

</body>
</html>

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
```

In the code above, we defined a function `filter_integers(values: List[Any]) -> List[int]` that takes a list of any type and returns a list of integers. The function uses list comprehension to iterate over the input list and includes a value in the output list if it is of type int, which is checked using the `isinstance()` function.

In the examples, the function is called with a list containing strings, floats, integers, dictionaries, and empty lists. The function correctly filters the integers out of the input lists and returns new lists containing only the integers.
"""

# Task 3:
# Create a function that calculates the sum of all numbers in a list.
# The list can contain nested lists and/or tuples.

```python
from typing import List, Union

def sum_nested(numbers: List[Union[int, List[int], Tuple[int]]]) -> int:
    total = 0
    for number in numbers:
        if isinstance(number, (list, tuple)):
            total += sum_nested(number)
        else:
            total += number
    return total

print