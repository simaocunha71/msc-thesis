from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]  # Output: [1, 2, 3]
print(filter_integers([1, 2, 3, 'abc', {}, [], 4.5, 5.5, 'hello']))  # Output: [1, 2, 3]  # Output: [1, 2, 3]
print(filter_integers([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(filter_integers(['a', 'b', 'c']))  # Output: []
print(filter_integers([True, False, None, 1, 2, 3]))  # Output: [1, 2, 3]  # Output: [1, 2, 3]
print(filter_integers([[], {}, 1, 2, 3, 'a', 'b', 'c']))  # Output: [1, 2, 3]  # Output: [1, 2, 3]
print(filter_integers(['1', '2', 3]))  # Output: [3]  # Output: [3]
print(filter_integers([1.0, 2.0, 3.0]))  # Output: []  # Output: []
print(filter_integers([True, 1, 2, 3, 'a']))  # Output: [1, 2, 3]  # Output: [1, 2, 3]
print(filter_integers([1, 2, 3, 'a', 'b', 'c', 4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]  # Output: [1, 2, 3, 4, 5, 6]
print(filter_integers([1, 2, 3, 4, 5, 6