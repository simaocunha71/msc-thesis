    arr = arr.copy()
    arr.sort()
    return sum(1 for a, b in zip(arr, arr[::-1]) if a != b) // 2


