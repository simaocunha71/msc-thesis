```python
def unique(l):
    return sorted(set(l))
```
This solution works by first converting the list to a set, which removes any duplicate elements. The set is then converted back to a list and sorted. This gives a list of unique elements in sorted order.

For example, if we call `unique([5, 3, 5, 2, 3, 3, 9, 0, 123])`, the function will return `[0, 2, 3, 5, 9, 123]`, which are the unique elements in the input list, in sorted order.