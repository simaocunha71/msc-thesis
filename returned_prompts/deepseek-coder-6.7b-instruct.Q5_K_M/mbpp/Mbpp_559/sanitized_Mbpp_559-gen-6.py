def max_sub_array_sum(lst: list, n: int) -> int:
    max_sum = 0
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j):
                curr_sum = curr_sum + lst[k]
            max_sum = max(max_sum, curr_sum)
    return max_sum