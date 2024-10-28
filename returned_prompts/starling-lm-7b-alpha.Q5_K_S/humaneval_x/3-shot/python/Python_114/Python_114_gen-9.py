    result = float('inf')
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if result > curr_sum:
            result = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return result


