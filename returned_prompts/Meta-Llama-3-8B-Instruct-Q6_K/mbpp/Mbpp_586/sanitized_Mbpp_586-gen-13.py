def split_Arr(arr, n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0 or n >= len(arr):
        raise ValueError("n is out of range")
    return arr[n:] + arr[:n]