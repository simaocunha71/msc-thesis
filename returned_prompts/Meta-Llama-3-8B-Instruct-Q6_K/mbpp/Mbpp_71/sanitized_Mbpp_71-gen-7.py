from random import randint
def comb_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    gap = len(arr)
    shrink = 1.3

    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)

        swapped = False
        for i in range(len(arr) - gap):
            j = i + gap
            if arr[i] > arr[j]:
                swap(i, j)
                swapped = True

    return arr