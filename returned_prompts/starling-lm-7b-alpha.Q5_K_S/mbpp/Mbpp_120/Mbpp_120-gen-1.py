from functools import reduce
from operator import mul

def max_product_tuple(tuples):
    return max(map(reduce, map(list, tuples), [mul]))


# Alternative approach
def max_product_tuple(tuples):
    from functools import reduce
    from operator import mul
    return reduce(lambda x, y: max(x, y), map(reduce, map(list, tuples), [mul]))


# Testing
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
assert max_product_tuple([(1, 1), (1, 1), (1, 1)]) == 1
assert max_product_tuple([(1, 1), (1, 1), (1, -1)]) == -1
```
    
```
"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

from functools import reduce
from operator import mul

def max_product_tuple(tuples):
    return max(map(reduce, map(list, tuples), [mul]))

# Alternative approach
def max_product_tuple(tuples):
    from functools import reduce
    from operator import mul
    return reduce(lambda x, y: max(x, y), map(reduce, map(list, tuples), [mul]))

# Testing
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
assert max_product_tuple([(1, 1), (1, 1), (1, 1)]) == 1
assert max_product_tuple([(1, 1), (1, 1), (1, -1)]) == -1
```
```

The provided Python code defines a function called `max_product_tuple` that takes a list of