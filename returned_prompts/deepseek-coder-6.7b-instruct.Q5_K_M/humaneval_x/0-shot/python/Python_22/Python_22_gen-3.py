from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]

print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))

# Output:
# [5]
# [1, 2, 3]

This solution uses list comprehension to iterate over the list of values. For each value, it checks if it is an instance of integer using the isinstance() function. If it is an integer, it includes it in the output list.

The function signature indicates that the function expects a list of Any type values and returns a list of integer values. The function is used to filter a list of values and return only the integers.

The docstring of the function provides an example of its usage and expected output.

The function is implemented in Python and uses the isinstance() function to check if a value is an integer. This function returns True if the specified object is of the specified type, otherwise False. In this case, it is used to check if each value in the list is an integer. If it is, the value is included in the new list. If not, it is not included.

The function is then tested with the provided examples and the expected output is printed.

The function is a simple and effective way to filter a list of values and return only the integers.

Overall, this solution is a good example of how to use Python's built-in functions and syntax to solve a problem.
