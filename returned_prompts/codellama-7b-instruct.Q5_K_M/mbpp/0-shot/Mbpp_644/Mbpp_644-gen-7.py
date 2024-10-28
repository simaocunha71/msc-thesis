```
def reverse_Array_Upto_K(arr, k):
    start = 0
    end = k
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
```
