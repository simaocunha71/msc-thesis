Here is the Python solution:
```python
def TotalMatch(lst1, lst2):
    sum1 = sum(len(s) for s in lst1)
    sum2 = sum(len(s) for s in lst2)
    if sum1 < sum2:
        return lst1
    elif sum1 > sum2:
        return lst2
    else:
        return lst1
```
Explanation:

1. We calculate the total number of characters in each list using a generator expression inside the `sum` function.
2. We compare the two sums. If `sum1` is less than `sum2`, we return `lst1`. If `sum1` is greater than `sum2`, we return `lst2`. If the sums are equal, we return `lst1` (since the problem statement says to return the first list in case of a tie).