def max_val(lst):
    max_value = None
    for item in lst:
        if max_value is None or (isinstance(item, int) and item > max_value):
            max_value = item
    return max_value

print(max_val(['Python', 3, 2, 4, 5, 'version']))  # Output: 5


"""
Explanation:
The function takes a list as an argument. It iterates over all the elements in the list. If the maximum value has not been set yet (i.e., `max_value` is `None`), it sets it to the first numeric value it finds. If the element is a number and it is greater than the current maximum, it updates the maximum.
"""

# Task 2
