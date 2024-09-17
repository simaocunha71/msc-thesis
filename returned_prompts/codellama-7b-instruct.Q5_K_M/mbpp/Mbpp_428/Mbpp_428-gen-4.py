
def shell_sort(arr):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def insertionSort(arr, gap):
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

    n = len(arr)
    gap = n // 2
    while gap > 0:
        insertionSort(arr, gap)
        gap = gap // 2

    return arr


