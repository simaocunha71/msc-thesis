def find_remainder(arr, n):
    result = 1
    for i in arr:
        result *= i
        result %= n
    return result