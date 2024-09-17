```
def pancake_sort(arr):
    for size in range(len(arr), 0, -1):
        max_index = 0
        for i in range(1, size):
            if arr[i] > arr[max_index]:
                max_index = i
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
            arr[:size] = arr[:size][::-1]
    return arr
```



This function implements the pancake sort algorithm. It works by repeatedly finding the maximum element in the unsorted part of the list and "flipping" it to the beginning of the unsorted part. This process is repeated until the entire list is sorted. The "flipping" is done by swapping the maximum element with the first element of the unsorted part, and then reversing the unsorted part to bring the maximum element to the beginning. The function returns the sorted list. The unit test provided ensures that the function works correctly for a list of integers.