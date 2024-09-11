def insert_element(lst, element):
    return [element]+lst


# Test
print(insert_element(['Red', 'Green', 'Black'],'c'))  # Output: ['c', 'Red', 'c', 'Green', 'c', 'Black']

























"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.

Examples:

insert_element(['Red', 'Green', 'Black'], 'c') --> returns ['c', 'Red', 'c', 'Green', 'c', 'Black']

insert_element([1, 2, 3], 0) --> returns [0, 1, 0, 2, 0, 3]

Note:

The input list will not be empty, and it will always contain at least one element.
"""

# Solution

def insert_element(lst, element):
    return [element]+lst

# Test
print(insert_element(['Red', 'Green', 'Black'],'c'))  # Output: ['c', 'Red', 'c', 'Green', 'c', 'Black']
print(insert_element([1, 2, 3], 0))  # Output: [0, 1, 0, 2, 0, 3]
```