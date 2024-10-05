from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]


print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

The function `filter_integers` uses a list comprehension to iterate over the elements of the input list and check if each element is an integer using the built-in `isinstance` function. If an element is an integer, it is included in the output list. If an element is not an integer, it is not included.

The `->` operator is used to denote the type of the return value of the function. In this case, the return type is `List[int]`, indicating that the function will return a list of integers. The `Any` type is used in the function signature to allow for any type of value in the input list.

This solution assumes that you want to filter out any non-integer values from the input list. If you instead want to include non-integer values, you can simply remove the `isinstance(value, int)` check from the list comprehension.

The `typing` module is used to provide type hints for the function arguments and return value. This can help with static type checking and IDE features.

Note: In Python 3.9 and later, you can use the `list[int]` syntax instead of `List[int]` for type hints. This is a more concise and readable alternative.


# 2. Write a Python function named `filter_integers` that takes a list of any python values as input and returns a list of integers.

