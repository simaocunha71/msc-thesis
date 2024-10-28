```
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
```


This function implements the shell sort algorithm, a variation of insertion sort that is more efficient for large datasets. The basic idea is to divide the array into subarrays, called "holes," and then sort each subarray individually using insertion sort.

The function takes an array as input, sorts it using shell sort, and returns the sorted array.

The unit test `assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]` ensures that the function works correctly. It checks that the output of the function is the same as the expected sorted array.

Note: The function does not handle edge cases such as an empty array or an array with duplicate elements. If you need to handle these cases, you can add additional code to handle them. For example, you can check if the array is empty and return an empty array if it is. You can also check if the array has duplicate elements and handle them accordingly.