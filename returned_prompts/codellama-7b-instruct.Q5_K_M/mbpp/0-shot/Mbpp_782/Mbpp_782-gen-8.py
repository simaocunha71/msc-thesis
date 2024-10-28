```
def odd_length_sum(arr):
    return sum(arr[i] for i in range(len(arr)) if len(arr[i:]) % 2)
```
