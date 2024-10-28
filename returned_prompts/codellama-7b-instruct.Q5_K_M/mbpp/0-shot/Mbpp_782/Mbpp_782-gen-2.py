```python
def odd_length_sum(arr):
    total = 0
    for i in range(1, len(arr)):
        for j in range(i, len(arr)):
            if j - i + 1 % 2 == 1:
                total += arr[j]
    return total
```
