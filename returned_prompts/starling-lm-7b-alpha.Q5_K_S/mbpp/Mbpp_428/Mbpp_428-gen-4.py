Here's a shell sort function in Python:

```python
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
                arr[j] = temp
        gap //= 2
    return arr
```

This function takes an array as input and sorts it using the shell sort algorithm. The `gap` variable is initially set to half the length of the array. The outer loop iterates through the array, and the inner loop compares each element with the elements that are `gap` positions ahead of it. If an element is smaller than the element it is compared with, they are swapped. This process is repeated until the array is fully sorted.

You can use the `assert` statement to test if the shell sort function correctly sorts the given array. In the provided example, the assertion `assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]` checks if the sorted array returned by the `shell_sort` function matches the expected sorted array `[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]`. If the assertion is true, it means that the shell sort function is working correctly.

It's worth noting that the shell sort algorithm has a worst-case and average time complexity of O(n log n). However, it may perform poorly on already sorted or reverse sorted arrays.

```python
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
