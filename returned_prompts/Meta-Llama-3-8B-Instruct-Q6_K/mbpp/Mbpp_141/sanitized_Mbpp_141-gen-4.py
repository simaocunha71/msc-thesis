def pancake_sort(arr):
    flips = []
    for i in range(len(arr)):
        max_idx = arr.index(max(arr[:i+1]))
        if max_idx != i:
            if max_idx != i:
                if max_idx != 0:
                    arr[:max_idx+1] = reversed(arr[:max_idx+1])
                arr[:i+1] = reversed(arr[:i+1])
            flips.extend([max_idx+1, i+1])
    return flips, arr