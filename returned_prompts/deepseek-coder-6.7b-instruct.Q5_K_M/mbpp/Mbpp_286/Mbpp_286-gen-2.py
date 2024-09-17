
def max_sub_array_sum_repeated(arr, n, k):
    total_sum = sum(arr)
    max_sum = cur_sum = sum(arr[:n])
    for i in range(n, len(arr)*k):
        cur_sum = cur_sum - arr[i % n] + arr[(i % n) + n]
        max_sum = max(max_sum, cur_us)
    return max_sum

