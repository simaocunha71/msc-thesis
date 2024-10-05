
Here is the solution:

```
def sort_array(array):
    if len(array) == 0:
        return []
    if sum(array[0], array[-1]) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)
```

Explanation:

*   We first check if the input array is empty. If it is, we simply return an empty list.
*   Then, we calculate the sum of the first element and the last element of the array. We use the modulo operator (`%`) to determine if the sum is even or odd.
*   If the sum is even, we sort the array in descending order using the `sorted` function with the `reverse=True` argument.
*   If the sum is odd, we sort the array in ascending order using the `sorted` function with no arguments.
*   Finally, we return the sorted array. The original array is not modified.