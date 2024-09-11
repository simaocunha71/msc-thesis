"""
Here is a way to do it:

def extract_singly(t):
    return reduce(lambda x, y: x + y, map(lambda x: x[0], t))

This can be done in Python 3.x using the built-in function reduce, which applies a function of two arguments cumulatively to the items of iterable, so as to reduce the iterable to a single output.

For example, if we have a list of numbers like this:

nums = [(3, 4, 5), (4, 5, 7), (1, 4)]

We can use reduce and map to apply the function lambda x: x[0] to each sublist of nums, which results in a new list of the first item of each sublist:

nums_flat = reduce(lambda x, y: x + y, map(lambda x: x[0], nums))

Finally, we can convert nums_flat to a set of unique numbers:

nums_flat = set(nums_flat)

And assert that the result is correct:

assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""

def extract_singly(t):
    return reduce(lambda x, y: x + y, map(lambda x: x[0], t))

# assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])

def flatten_list(t):
    return reduce(lambda x, y: x + y, map(lambda x: x[0], t))

# assert set(flatten_list([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])


# Made By Mostafa_Khaled
```
python
    
"""
Write a function to fl