def max_sub_array_sum_repeated(arr: list, k: int, m: int) -> int:
    n = len(arr)
    max_sum = float('-inf')
    for _ in range(k):
        curr_sum = 0
        for i in range(n):
            curr_sum += arr[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        arr = arr[1:] + [arr[0]]
    return max_sum