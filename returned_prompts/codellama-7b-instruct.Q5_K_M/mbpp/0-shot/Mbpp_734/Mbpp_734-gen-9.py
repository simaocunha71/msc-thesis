```
def sum_Of_Subarray_Prod(arr):
    return sum([reduce(lambda x, y: x * y, arr[i:]) for i in range(len(arr))])
```
