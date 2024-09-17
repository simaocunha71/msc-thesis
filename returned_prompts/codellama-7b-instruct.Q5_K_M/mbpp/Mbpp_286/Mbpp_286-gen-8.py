
def max_sub_array_sum_repeated(arr, k, n):
    max_sum = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n + i):
            curr_sum += arr[j % n]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum * k


