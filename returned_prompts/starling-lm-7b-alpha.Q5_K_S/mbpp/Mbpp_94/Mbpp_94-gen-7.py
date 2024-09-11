"""
def index_minimum(tuples):
    # Find the tuple with the smallest second value
    min_index = min(tuples, key=lambda x: x[1])[0]
    return min_index

# Tests
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
assert index_minimum([('John', 100), ('Jane', 140), ('Jacob', 100)]) == 'John'
"""

In this solution, we use the built-in `min` function to find the tuple with the smallest second value. The `min` function takes an iterable (in this case, a list of tuples) and a key function to determine the smallest value. We pass a lambda function that returns the second value of each tuple, so `min` will find the tuple with the smallest second value. Then, we use indexing to get the first value of that tuple and return it.

Here's how the code works step by step:

1. The `index_minimum` function takes the `tuples` list as an argument.
2. We use the `min` function to find the tuple with the smallest second value. We pass a lambda function as the `key` argument to `min` to specify that we want to compare the second value of each tuple. The `min` function returns the tuple with the smallest second value.
3. We use indexing to get the first value of the tuple with the smallest second value. Since Python uses zero-based indexing, we use `[0]` to get the first value.
4. Finally, we return the first value of the tuple with the smallest second value.

The code includes two tests to check if the `index_minimum` function is working correctly. The first test checks if the function correctly returns 'Varsha' when given the list `[('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]`. The second test checks if the function correctly returns 'John' when given the list `[('John', 100), ('Jane', 140), ('Jacob', 1