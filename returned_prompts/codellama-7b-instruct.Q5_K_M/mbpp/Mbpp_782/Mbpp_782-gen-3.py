```python
def odd_length_sum(arr):
    return sum(arr[i:i+3] for i in range(len(arr)-2) if len(arr[i:i+3])%2==1)
```
