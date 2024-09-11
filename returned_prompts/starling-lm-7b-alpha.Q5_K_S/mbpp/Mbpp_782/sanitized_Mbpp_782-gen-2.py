def odd_length_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]
    if n == 3:
        return arr[0] + arr[1] + arr[2]
    if n % 2 == 0:
        return odd_length_sum(arr[:-1]) + arr[-1] + arr[0]
    else:
        return odd_length_sum(arr[:-1]) + arr[-1] + arr[0] + sum(arr[1:-1:2])