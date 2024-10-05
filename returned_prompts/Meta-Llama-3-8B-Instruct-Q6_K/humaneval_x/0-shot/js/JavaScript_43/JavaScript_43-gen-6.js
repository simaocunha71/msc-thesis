Here is a Python solution:

```python
def pairsSumToZero(l):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False
```

This function works by iterating over the list and checking if the negation of each number is in the set `seen`. If it is, that means we've found a pair that sums to zero, so we return `True`. If we get through the entire list without finding such a pair, we return `False`. This function has a time complexity of O(n), where n is the length of the input list, because we're doing a single pass over the list. It has a space complexity of O(n), because in the worst case (when all numbers are distinct) we'll need to store all n numbers in the set `seen`. 