```python
from itertools import chain, combinations

def combinations_list(lst):
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

print(combinations_list(['orange', 'red', 'green', 'blue']))
```

This function uses the built-in Python library `itertools` to generate all possible combinations of elements in the given list. The `chain.from_iterable` function is used to flatten the list of combinations into a single list.

The `combinations` function is used to generate all possible combinations of the elements of the input list for lengths ranging from 0 to the length of the list. The `range(len(lst)+1)` generates these lengths. The `chain.from_iterable` function is used to flatten the list of combinations into a single list.
"""

# 4
