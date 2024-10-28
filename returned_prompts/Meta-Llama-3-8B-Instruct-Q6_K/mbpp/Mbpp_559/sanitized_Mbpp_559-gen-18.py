def max_sub_array_sum(lst, n):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(lst)):
        current_sum += lst[i]
        if i >= n:
            current_sum -= lst[i-n]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum