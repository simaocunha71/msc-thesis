Here is the Python code for the problem:

```python
def maximum(arr, k):
    if k == 0:
        return []
    if k >= len(arr):
        return sorted(arr)
    return sorted(arr, reverse=True)[:k]
```

In this code, we first check if k is 0, in which case we return an empty list. If k is greater than or equal to the length of the array, we return the sorted array. Otherwise, we sort the array in reverse order and return the first k elements.