```
def find_min_diff(arr,n):
    arr.sort()
    min_diff = float("inf")
    for i in range(n-1):
        min_diff = min(min_diff,arr[i+1]-arr[i])
    return min_diff
```
