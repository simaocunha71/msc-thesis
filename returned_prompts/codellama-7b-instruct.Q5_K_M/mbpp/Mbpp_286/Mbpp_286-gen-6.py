```python
def max_sub_array_sum_repeated(arr, k, m):
    return max(
        sum(arr[i:i+m] for i in range(0, len(arr)-m+1))
        for _ in range(k)
    )
```
