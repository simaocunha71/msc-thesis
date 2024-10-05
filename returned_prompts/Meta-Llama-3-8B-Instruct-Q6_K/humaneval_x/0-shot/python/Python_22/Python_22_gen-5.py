from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    """
    return [value for value in values if isinstance(value, int)]


# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers(['a', 3.14, 'c', 5, 6]))  # Output: [5, 6]
print(filter_integers([1, 2, 3, 'abc', 4.5, 6]))  # Output: [1, 2, 3, 6]
print(filter_integers([1, 2, 3, 'abc', 4, 5.6]))  # Output: [1, 2, 3, 4]
print(filter_integers(['a', 3.14, 'c', 5, 'd', 6]))  # Output: [5, 6]





# Test the function
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers(['a', 3.14, 'c', 5, 6]))  # Output: [5, 6]
print(filter_integers([1, 2, 3, 'abc', 4.5, 6]))  # Output: [1, 2, 3, 6]
print(filter_integers([1, 2, 3, 'abc', 4, 5.6]))  # Output: [1, 2, 3, 4]
print(filter_integers(['a', 3.14, 'c', 5, 'd', 6]))  # Output: [5, 6]
print(filter_integers([1, 'a', 2, 3, 'b', 4]))  # Output: [1, 2, 3, 4]
print(filter_integers(['a', 'b', 'c', 1