def max_sum(arr):
    arr.sort()
    return max(arr[-1] - arr[0], sum(arr[1:-1]))



