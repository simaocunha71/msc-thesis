"""
Firstly, let's understand the problem.

The problem is to find the number of unordered pairs in the given list where both elements are unequal. 

For example, in the list [1, 2, 1], the pairs are (1, 2) and (1, 1).

We can solve this problem using two nested loops in python. 

The outer loop picks an element from the list and the inner loop picks all the elements after the outer loop's picked element. 

We compare the picked elements in the outer loop and inner loop. If they are unequal, we increment the count.

This problem can also be solved using the combinations method from the itertools module in python. 

We use combinations to get all the possible pairs from the list and then we filter out the pairs where both elements are unequal.
"""

Solution using two nested loops:

```python
def count_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_pairs([1, 2, 1]))  # Output: 2
```

Solution using itertools.combinations:

```python
from itertools import combinations

def count_pairs(lst):
    return sum(1 for a, b in combinations(lst, 2) if a != b)

print(count_pairs([1, 2, 1]))  # Output: 2
```
"""

def count_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    return count

print(count_pairs([1, 2, 1]))  # Output: 2

from itertools import combinations

def count_pairs(lst):
    return sum(1 for a, b in combinations(lst, 2