from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if type(value) == int]


print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))


Output:
[5]
[1, 2, 3]


The function filter_integers uses list comprehension to iterate over the given list of values. It checks if the type of each value is int using the built-in type() function. If it is, the value is included in the new list. If not, it is ignored.

This code is written in Python 3.6, and it uses the type hinting feature introduced in Python 3.5. Type hinting is a way to specify the expected types of function arguments and return values. In this case, the function filter_integers is annotated with the expected types of its arguments and return value.

The function filter_integers returns a list of integers that are found in the given list of values. If no integers are found, an empty list is returned.

Please note that the type hinting feature is not enforced by Python. It is optional and used by some tools for static type checking. However, it doesn't stop the program from running if the types are not as expected.
"""

from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if type(value) == int]


print(filter_integers(['a', 3.14, 5]))
print(filter_integers([1, 2, 3, 'abc', {}, []]))
<jupyter_output>
[5]
[1, 2, 3]
<jupyter_text>
