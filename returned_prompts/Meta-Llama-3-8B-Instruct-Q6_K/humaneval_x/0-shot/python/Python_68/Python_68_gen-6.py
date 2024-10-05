The solution to this problem involves iterating through the array to find the smallest even value and its index. Here's the Python code for the problem:

```python
def pluck(arr):
    smallest_even_value = float('inf')
    smallest_even_index = -1
    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_value:
            smallest_even_value = value
            smallest_even_index = i
    if smallest_even_value == float('inf'):
        return []
    return [smallest_even_value, smallest_even_index]
```

This function iterates through the array using the `enumerate` function, which returns both the index and the value of each element. It checks if the value is even and if it is smaller than the current smallest even value. If it is, it updates the smallest even value and its index. After iterating through the entire array, it checks if the smallest even value is still infinity, which means that there were no even values in the array. If that's the case, it returns an empty list. Otherwise, it returns a list containing the smallest even value and its index. 