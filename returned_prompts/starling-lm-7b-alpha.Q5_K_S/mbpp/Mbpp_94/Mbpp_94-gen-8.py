"""
Here's one way to solve this problem:

1. Initialize a variable called `min_val` to the first tuple in the list. Set its value to `(None, None)`. This will be the minimum value we find.
2. Initialize a variable called `min_val_index` to 0. This is the index of the tuple that currently has the minimum value.
3. Loop through the list of tuples using the `enumerate()` function. For each tuple, do the following:
   a. Compare the second value of the tuple to the second value of `min_val`. If the second value of the tuple is less than the second value of `min_val`, update `min_val` to be the tuple, and update `min_val_index` to be the index of the tuple.
4. After the loop, `min_val` will be the tuple with the smallest second value, and `min_val_index` will be the index of that tuple in the original list. Return `min_val[0]`.

Here's the code:
"""

def index_minimum(lst):
    min_val = (None, None)
    min_val_index = 0
    for i, t in enumerate(lst):
        if t[1] < min_val[1]:
            min_val = t
            min_val_index = i
    return min_val[0]

# Test the function
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'

# More tests
assert index_minimum([(4, 2), (3, 4), (7, 1), (5, 3), (8, 1)]) == 3
assert index_minimum([(3, 100), (2, 50), (1, 200), (0, 10)]) == 0
assert index_minimum([(5, 200), (4, 300), (3, 100), (2, 400), (1, 200)]) == 3

#