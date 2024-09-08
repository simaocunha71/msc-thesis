
```python
from itertools import chain, combinations

def find_combinations(lst):
    all_combinations = list(chain(*map(lambda x: combinations(x, 2), lst)))
    sums = [(x[0]+y[0], x[1]+y[1]) for x, y in combinations(all_combinations, 2) if x[0]+y[0] <= 12 and x[1]+y[1] <= 12]
    return sums

assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
```

This solution first finds all possible combinations of 2-tuples from the given list, then finds all combinations of 2-tuples from all combinations. It then filters out the combinations that do not sum to values less than or equal to 12.
"""

