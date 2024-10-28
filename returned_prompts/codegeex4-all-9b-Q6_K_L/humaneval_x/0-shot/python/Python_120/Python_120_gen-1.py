```python
def maximum(arr, k):
    if k == 0:
        return []
    if k >= len(arr):
        return sorted(arr)
    return sorted(arr)[-k:]
```

Explanation:
- If k is 0, return an empty list.
- If k is greater than or equal to the length of the array, return a sorted version of the array.
- Otherwise, return the last k elements of the array, sorted.