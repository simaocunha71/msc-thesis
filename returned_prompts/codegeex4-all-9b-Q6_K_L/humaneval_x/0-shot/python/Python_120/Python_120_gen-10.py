Here is the Python code for the problem:

```python
def maximum(arr, k):
    if k == 0:
        return []
    if k >= len(arr):
        return sorted(arr)
    else:
        return sorted(arr, reverse=True)[:k]
```

This function works by first checking if `k` is equal to 0. If it is, it returns an empty list. Then, it checks if `k` is greater than or equal to the length of `arr`. If it is, it returns a sorted version of `arr` in descending order. Otherwise, it returns the first `k` elements of a sorted version of `arr` in descending order.