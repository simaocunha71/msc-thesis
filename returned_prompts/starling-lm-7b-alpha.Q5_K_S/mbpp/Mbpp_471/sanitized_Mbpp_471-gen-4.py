def find_remainder(arr, mod):
    if len(arr) == 1:
        return arr[0] % mod
    else:
        return (find_remainder(arr[1:], mod) * arr[0]) % mod