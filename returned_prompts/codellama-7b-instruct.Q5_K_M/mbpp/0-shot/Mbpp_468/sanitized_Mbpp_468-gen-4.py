def max_product(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])
    else:
        max_left = max_product(arr[:-1])
        max_right = max_product(arr[1:])
        max_mid = max(arr[-1], arr[-2])
        return max(max_left * max_mid, max_right * max_mid)