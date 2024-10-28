def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """

    # Create a new list to hold the integers
    integers = []

    # Iterate through the list of values
    for value in values:
        # Check if the value is an integer
        if isinstance(value, int):
            # If it is, add it to the list
            integers.append(value)
    return integers


# Use the function to filter a list of values for integers
filtered_list = filter_integers(['a', 3.14, 5])
print(filtered_list)  # Output: [5]

filtered_list = filter_integers([1, 2, 3, 'abc', {}, []])
print(filtered_list)  # Output: [1, 2, 3]


# Test the function with a list of values that are all integers
filtered_list = filter_integers([1, 2, 3, 4, 5])
print(filtered_list)  # Output: [1, 2, 3, 4, 5]


# Test the function with an empty list
filtered_list = filter_integers([])
print(filtered_list)  # Output: []



# Test the function with a list of values that are all floats
filtered_list = filter_integers([1.1, 2.2, 3.3])
print(filtered_list)  # Output: []



# Test the function with a list of values that are all strings
filtered_list = filter_integers(['abc', 'def', 'ghi'])
print(filtered_list)  # Output: []



# Test the function with a list of values that are all dictionaries
filtered_list = filter_inte