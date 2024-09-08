def sort_matrix(matrix):
    return sorted(matrix, key=sum)

print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))

"""
Explanation:
The key parameter in the sorted function is a function that takes an item from the list and returns a value that will be used for sorting purposes. In this case, we're using the sum function, which returns the sum of a list. This means that the list will be sorted based on the sum of the rows.
"""

# Q2
"""
Write a Python function that takes in a list and returns a dictionary where the keys are the elements of the list and the values are their corresponding count in the list.
assert get_count([1, 1, 2, 2, 2, 3]) == {1: 2, 2: 3, 3: 1}
"""

# A2
def get_count(lst):
    return {i: lst.count(i) for i in lst}

print(get_count([1, 1, 2, 2, 2, 3]))

# Q3
"""
Write a Python function that takes in a list of tuples and returns a dictionary where the keys are the first elements of the tuples and the values are the corresponding second elements.
assert convert_to_dict([(1, 'a'), (2, 'b'), (3, 'c')]) == {1: 'a', 2: 'b', 3: 'c'}
"""

# A3
def convert_to_dict(lst):
    return {i[0]: i[1] for i in lst}

print(convert_to_dict([(1, 'a'), (2, 'b'), (3, 'c')]))

# Q4
"""
Write a Python function that takes in a list of integers and returns a list of only the unique elements in the list.
assert get_unique([1, 2, 2, 3, 4, 4, 4, 5]) == [1, 2, 3, 4, 5]
"""

