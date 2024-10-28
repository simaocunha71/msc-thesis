Here's one possible implementation in Python:

```python
def add_elements(arr, k):
    total = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total
```

This function iterates over the first k elements of the input array `arr` and adds up the elements that have at most two digits. The `len(str(arr[i])) <= 2` condition checks if the number of digits in the current element is less than or equal to 2. If it is, the element is added to the total sum. Finally, the function returns the total sum.