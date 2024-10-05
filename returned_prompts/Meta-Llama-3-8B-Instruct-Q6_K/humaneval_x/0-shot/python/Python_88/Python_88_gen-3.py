
The problem requires you to create a function called `sort_array` that takes an array of non-negative integers as input and returns a copy of the array after sorting. The array should be sorted in ascending order if the sum of the first and last elements is odd, and in descending order if the sum is even.

Here is the solution:

```python
def sort_array(array):
    if len(array) == 0:
        return array

    sum_first_last = array[0] + array[-1]

    if sum_first_last % 2 == 0:
        array = sorted(array, reverse=True)
    else:
        array = sorted(array)

    return array.copy()
```

This function first checks if the array is empty. If it is, the function returns the array as it is. Then, it calculates the sum of the first and last elements of the array.

If the sum is even, the function sorts the array in descending order using the `sorted` function with the `reverse=True` argument. If the sum is odd, the function sorts the array in ascending order using the `sorted` function without any arguments.

Finally, the function returns a copy of the sorted array using the `copy` method. This is necessary because the problem statement asks you to return a copy of the array, not the original array. This ensures that the original array remains unchanged.