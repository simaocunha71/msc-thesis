```
def pancake_sort(arr):
    for size in range(len(arr), 0, -1):
        max_index = arr.index(max(arr[:size]))
        if max_index != size - 1:
            if max_index != 0:
                arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:size] = arr[:size][::-1]
    return arr
```






The function `pancake_sort` takes a list of elements and sorts it in ascending order using the pancake sorting algorithm. The function iterates over the list from the end to the start, finding the maximum element in each iteration and flipping it to the end of the list if necessary. The function uses slicing to reverse the list and to find the maximum element. The function returns the sorted list.