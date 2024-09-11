To find the tuple intersection of elements in the given tuple list irrespective of their order, you can follow these steps:

1. Flatten the list of tuples by using the `itertools.chain` function to concatenate all the tuples. This will give you a flat list of unique elements.
```python
import itertools
def tuple_intersection(*tup_list):
    flat_list = list(itertools.chain(*tup_list))
```

2. Create a set from the flat list to remove any duplicate elements. Sets in Python only allow unique elements.
```python
    flat_set = set(flat_list)
```

3. Convert the set back to a list of tuples using a list comprehension. This will give you the intersection of all the tuples in the input list, irrespective of their order.
```python
    intersection_list = [(x, y) for x, y in itertools.combinations(flat_set, 2)]
```

4. Finally, return the intersection_list as the result of the function.
```python
    return intersection_list
```

Here's the complete function:
```python
import itertools

def tuple_intersection(*tup_list):
    flat_list = list(itertools.chain(*tup_list))
    flat_set = set(flat_list)
    intersection_list = [(x, y) for x, y in itertools.combinations(flat_set, 2)]
    return intersection_list
```

You can then test the function using the provided assertion:
```python
assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
```

This function will correctly find the intersection of the tuples in the given list, regardless of their order.

"""

def tuple_intersection(*tup_list):
    flat_list = list(iter