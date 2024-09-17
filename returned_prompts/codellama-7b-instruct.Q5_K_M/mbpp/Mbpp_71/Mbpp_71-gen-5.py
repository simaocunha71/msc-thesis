
def comb_sort(arr: list):
    gap = len(arr)
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / 1.25)
        if gap < 1:
            gap = 1
        swapped = False
        for i in range(len(arr) - gap):
            if arr[i] < arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr


