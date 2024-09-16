```
def max_product(arr):
    if not arr:
        return 0
    max_val = 1
    for i in range(len(arr)):
        max_val *= arr[i]
        if max_val == 0:
            break
    min_val = 1
    for i in range(len(arr) - 1, -1, -1):
        min_val *= arr[i]
        if min_val == 0:
            break
    return max(max_val, min_val)
```

