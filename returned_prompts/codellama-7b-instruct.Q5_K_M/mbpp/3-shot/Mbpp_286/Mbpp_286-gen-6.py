
def max_sub_array_sum_repeated(arr: list, k: int, n: int) -> int:
    max_sum = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if (j - i + 1) % k == 0:
                max_sum = max(max_sum, curr_sum)
    return max_sum


