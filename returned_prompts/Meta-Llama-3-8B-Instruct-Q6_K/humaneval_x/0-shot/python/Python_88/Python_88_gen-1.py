
The problem can be solved by first checking if the length of the array is 0. If it is, the function simply returns the original array.

Next, the function calculates the sum of the first and last elements of the array. If the sum is even, it sorts the array in descending order. If the sum is odd, it sorts the array in ascending order.

Finally, the function returns the sorted array.

Here is the Python code that implements this solution:

```python
def sort_array(array):
    if len(array) == 0:
        return array

    sum_first_last = array[0] + array[-1]
    if sum_first_last % 2 == 0:
        sorted_array = sorted(array, reverse=True)
    else:
        sorted_array = sorted(array)

    return sorted_array
```

This code defines a function `sort_array` that takes an array as input and returns a sorted copy of the array. The function first checks if the array is empty, and if so, returns the original array. Then it calculates the sum of the first and last elements of the array, and uses this sum to determine whether to sort the array in ascending or descending order. Finally, it returns the sorted array.