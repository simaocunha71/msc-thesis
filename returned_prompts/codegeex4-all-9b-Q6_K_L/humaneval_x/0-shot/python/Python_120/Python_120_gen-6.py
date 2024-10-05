```python
def maximum(arr, k):
    if k == 0:
        return []
    arr.sort(reverse=True)
    return arr[:k]
```
