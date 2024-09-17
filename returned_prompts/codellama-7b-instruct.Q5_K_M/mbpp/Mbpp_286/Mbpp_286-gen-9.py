
def max_sub_array_sum_repeated(arr, k, n):
    largest = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if (j - i + 1) % k == 0:
                largest = max(largest, curr_sum)
    return largest


