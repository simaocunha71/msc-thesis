def pancake_sort(arr):
    def flip(subarr):
        subarr.reverse()

    for i in range(len(arr) - 1, -1, -1):
        max_idx = arr.index(max(arr[:i + 1]))
        if max_idx != i:
            flip(arr[:max_idx + 1])
            flip(arr[:i + 1])

    return arr