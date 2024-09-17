def max_sub_array_sum(nums, k: int) -> int:
    max_sum = 0
    current_sum = 0
    for num in nums:
        current_sum = max(current_sum + num, num)
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum == k:
            break
    return max_sum