def find_remainder(arr, mod):
    result = 1
    for i in arr:
        result = (result * i) % mod
    return result