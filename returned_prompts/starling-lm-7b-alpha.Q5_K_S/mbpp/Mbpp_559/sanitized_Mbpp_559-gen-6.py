def max_sub_array_sum(numbers, target):
    max_sum = 0
    for i in range(len(numbers)):
        curr_sum = 0
        for j in range(i, len(numbers)):
            curr_sum += numbers[j]
            if curr_sum == target:
                max_sum = max(max_sum, curr_sum)
    return max_sum