from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1.0, 2.0, 3.0, 4, 5]))  # [4, 5]  # 4 and 5 are integers, 1.0, 2.0, 3.0 are floats
print(filter_integers([True, False, 1, 2, 3]))  # [1, 2, 3]  # True and False are booleans, 1, 2, 3 are integers
print(filter_integers(['a', 'b', 'c']))  # []  # all values are strings
print(filter_integers([1, 2, 3, 'a', 'b', 'c']))  # [1, 2, 3]  # 1, 2, 3 are integers, 'a', 'b', 'c' are strings
print(filter_integers([1, 2, 3, 4.5, 5]))  # [1, 2, 3, 5]  # 1, 2, 3 are integers, 4.5 is a float, 5 is an integer
print(filter_integers([True, False, 1.0, 2.0, 3.0, 4, 5]))  # [4, 5]  # 4, 5 are integers, True, False are booleans, 1.0, 2.0, 3.0 are floats
print(filter_integers([]))  # []  # empty list
print(filter_integers([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]  # all values are integers

# Test case with a list of mixed types
print(filter_integers([1, 'a', 2.0, 3, True, 4, 'b', 5.0, 6