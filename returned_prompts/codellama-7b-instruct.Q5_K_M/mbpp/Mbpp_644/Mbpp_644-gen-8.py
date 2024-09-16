```python
def reverse_Array_Upto_K(arr,k):
    for i in range(0,k):
        arr[i],arr[k-i-1] = arr[k-i-1],arr[i]
    return arr
```