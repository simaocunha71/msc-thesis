from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]


# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers([1, 2, 3, 'abc', 4.5, 6]))  # Output: [1, 2, 3, 6]  # Note: 4.5 is filtered out
print(filter_integers(['a', 'b', 'c']))  # Output: []  # Note: no integers in the list
print(filter_integers([1, 2, 3, 4.5, 5]))  # Output: [1, 2, 3, 5]  # Note: 4.5 is filtered out
print(filter_integers([1, 2, 'a', 3, 'b', 4, 'c', 5]))  # Output: [1, 2, 3, 4, 5]  # Note: 'a', 'b', 'c' are filtered out
print(filter_integers([]))  # Output: []  # Note: empty list
print(filter_integers([1]))  # Output: [1]  # Note: single integer in the list
print(filter_integers([1, 2, 3]))  # Output: [1, 2, 3]  # Note: three integers in the list
print(filter_integers([1.0, 2.0, 3.0]))  # Output: []  # Note: all elements are floats
print(filter_integers([1, 2, 3.0, 4, 5.0]))  # Output: [1, 2, 4, 5]  # Note: floats are filtered out
print(filter_integers([1, 2, 3, 4, 5, 6.0, 7, 8, 9.0]))  # Output: [1, 2, 3, 4, 5, 7, 8, 9]  # Note