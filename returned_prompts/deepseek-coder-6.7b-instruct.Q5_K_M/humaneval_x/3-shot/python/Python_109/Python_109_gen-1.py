    shifted = arr[1:] + arr[:1]
    return shifted == sorted(arr) or arr == sorted(arr)

