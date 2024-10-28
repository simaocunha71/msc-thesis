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


The shell sort algorithm starts by setting a gap equal to half the size of the array. It then iterates over the array, comparing elements that are a gap distance apart. If an element is smaller than the one before it, they are swapped.

This process is repeated until the gap is 0, at which point the array is sorted.

The provided unit test shows that the function correctly sorts the given array. For example, the test `assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]` checks that the function returns the correct sorted array.