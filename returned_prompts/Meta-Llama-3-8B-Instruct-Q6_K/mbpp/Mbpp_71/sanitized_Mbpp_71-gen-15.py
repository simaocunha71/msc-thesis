def comb_sort(arr):
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    gap = len(arr)
    shrink = 1.3

    while not is_sorted(arr):
        gap = int(gap / shrink)
        if gap > 1:
            for i in range(len(arr) - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
        else:
            gap = 1

    return arr