def find_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result