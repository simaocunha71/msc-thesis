
def max_sum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1], arr[0] + arr[1])
    if n == 3:
        return max(arr[0], arr[1] + arr[2], arr[2], arr[0] + arr[1])
    max_sum_left = max_sum(arr[:n//2])
    max_sum_right = max_sum(arr[n//2:])
    max_sum_middle = max(arr[n//2-1:]) + max(arr[:n//2])
    return max(max_sum_left, max_sum_right, max_sum_middle)


