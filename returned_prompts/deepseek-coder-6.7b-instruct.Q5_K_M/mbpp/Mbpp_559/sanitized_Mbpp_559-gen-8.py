def max_sub_array_sum(lst, n):
    max_sum = 0
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += lst[j]
            max_sum = max(sum_, max_sum)
    return max_sum