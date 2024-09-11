def index_minimum(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])[0][0]

print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]))




"""
Correct Solution:
def index_minimum(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])[0][0]
"""

"""
Incorrect Solution:
def index_minimum(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])[1][0]
"""

# Here's a detailed explanation of the solution:

# The `sorted()` function in Python is used to sort the list of tuples based on the second value of each tuple. The `key` parameter of the `sorted()` function is used to specify the attribute to be considered for sorting. In this case, `key=lambda x: x[1]` specifies that the second element of each tuple should be considered for sorting.

# The `lambda` function is an anonymous function in Python, which is used here to define a simple function that takes a tuple `x` as input and returns its second element `x[1]`.

# The `sorted()` function returns a new list that contains the sorted tuples. We can then access the first tuple of this sorted list using indexing `[0]` and the first element of this tuple using indexing `[0]` again.

# This solution will return the first value of the tuple with the smallest second value, as required by the problem statement.

# Note that the incorrect solution `return sorted(list_of_tuples, key=lambda x: x[1])[1][0]` would return the second tuple of the sorted list, which is incorrect according to the problem statement.
"""

# Here's a detailed explanation of the solution:

# The `sorted()` function in Python is used to sort the list of tuples based on the second value of each tuple. The `key` parameter of the