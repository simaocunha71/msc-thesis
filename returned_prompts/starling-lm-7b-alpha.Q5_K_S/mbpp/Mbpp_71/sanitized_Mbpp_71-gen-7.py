def comb_sort(arr):
    n = len(arr)

    gap = n
    swapped = True
    while gap != 1 or swapped == True:
        gap = comb_gap(gap, n)
        swapped = False

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr
def comb_gap(gap, n):
    return int(gap * 10 / 13 + 1) if gap % 13 != 0 else int(gap / 13)