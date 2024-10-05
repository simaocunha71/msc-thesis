from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(filter_integers(['a', 'b', 'c']))  # []


# Explanation:
# This function uses list comprehension to iterate over the given list of any python values.
# It uses the isinstance() function to check if each value is an integer.
# If the value is an integer, it is included in the new list.
# Finally, the function returns the new list containing only the integers from the original list.