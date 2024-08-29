You can use itertools.combinations function to get all possible combinations of tuples and then find the sum of each combination.

Here is the python code for it:

```python
from itertools import combinations

def find_combinations(lst):
    combs = []
    for i in range(1, len(lst) + 1):
        combs.extend(combinations(lst, i))
    sums = [(sum(x[0] for x in comb), sum(x[1] for x in comb)) for comb in combs]
    return sums
```

In the given example, [(2, 4),  (6, 7),  (5, 1),  (6, 10)] is passed to the function, and it returns a list of tuples where each tuple is a combination of sums from the given list of tuples. The order of numbers in each tuple doesn't matter, so (2, 4) is the same as (4, 2).

The function works by first getting all combinations of tuples (from 1 to the length of the given list) and then calculating the sum of each combination. The sums are returned as a list of tuples.

Note: This function will return duplicates if the input list contains duplicate tuples. For example, if the input list is [(2, 4), (2, 4)], the output will contain both (4, 8) and (4, 8).
"""

