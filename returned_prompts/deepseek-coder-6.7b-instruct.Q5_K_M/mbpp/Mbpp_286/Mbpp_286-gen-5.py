
def max_sub_array_sum_repeated(arr: list, k: int) -> int:
    n = len(arr)
    max_sum = -999999999999
    for i in range(k):
        curr_sum = 0
        for j in range(n):
            curr_sum += arr[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
    return max_sum


