```
def extract_even(tup):
    result = ()
    for element in tup:
        if isinstance(element, tuple):
            element = extract_even(element)
        elif element % 2 == 0:
            result += (element,)
    return result
```
The problem is asking to create a function that takes a nested mixed tuple as an input and returns a new tuple containing only the even elements from the original tuple. The function should recursively traverse the nested tuples and extract the even elements.

The unit test `assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)` helps to understand the problem better. It shows that the function should recursively traverse the nested tuples and extract the even elements.

Here's a Python solution for the problem:
```
def extract_even(tup):
    result = ()
    for element in tup:
        if isinstance(element, tuple):
            element = extract_even(element)
        elif element % 2 == 0:
            result += (element,)
    return result
```
This function iterates over each element in the input tuple. If the element is a tuple itself, the function calls itself recursively to extract the even elements from the nested tuple. If the element is even, it is added to the result tuple. The function finally returns the result tuple containing only the even elements from the original tuple.