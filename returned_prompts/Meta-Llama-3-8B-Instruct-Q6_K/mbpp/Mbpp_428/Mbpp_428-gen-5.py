```
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
```


The shell sort algorithm is a simple sorting algorithm that is based on the insertion sort algorithm. It works by first dividing the array into a number of subarrays, called "runs", and then sorting each run using insertion sort. The size of the runs is reduced by half in each iteration until only one run remains, which is then sorted using insertion sort.

The `shell_sort` function implements the shell sort algorithm. It takes an array as input and returns the sorted array. The function first calculates the initial gap size, which is half the length of the array. It then enters a loop that continues until the gap size is 0. In each iteration of the loop, the function sorts the array using insertion sort, but instead of comparing each element with every other element, it only compares elements that are gap positions apart. The function then reduces the gap size by half and repeats the process until the gap size is 0.

The unit test `assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]` demonstrates the correctness of the `shell_sort` function. The function correctly sorts the input array and returns the sorted array.