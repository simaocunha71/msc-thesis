def comb_sort(arr):
    gap = len(arr)
    swapped = True
    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))  
        swapped = False
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr_[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr