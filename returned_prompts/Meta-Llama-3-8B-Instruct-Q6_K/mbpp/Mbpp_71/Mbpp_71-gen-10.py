```
def comb_sort(arr):
    if not arr:
        return []

    gap = len(arr)
    shrink = 1.3

    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)

        if gap < 1:
            gap = 1

        swapped = False

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    return arr
```


This function implements the Comb Sort algorithm, which is a variation of the Bubble Sort algorithm. It uses a gap size to control the iteration, and the gap size is decreased by a factor of shrink for each iteration until it reaches 1. The function sorts the array in-place and returns the sorted array. The unit test provided ensures that the function works correctly for the given input.