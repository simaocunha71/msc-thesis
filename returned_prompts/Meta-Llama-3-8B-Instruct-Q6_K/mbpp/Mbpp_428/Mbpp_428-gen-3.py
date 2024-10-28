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



The provided unit test `assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]` ensures that the function correctly sorts the given array using the shell sort algorithm. The shell sort algorithm is an in-place comparison-based sorting algorithm that uses a gap to divide the array into smaller subarrays, sorts each subarray, and then gradually reduces the gap until the entire array is sorted. In this implementation, the gap is initialized as half of the array length, and it is reduced by half in each iteration until it becomes 0. The array is then iteratively sorted by comparing elements at the current gap distance and swapping them if they are in the wrong order. The function returns the sorted array.