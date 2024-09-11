def odd_length_sum(nums):
    """
    Find the sum of all odd length subarrays of nums.
    """
    total_sum = 0
    for start_index in range(len(nums)):
        for end_index in range(start_index + 1, len(nums) + 1):
            total_sum += sum(nums[start_index:end_index])
            if (end_index - start_index) % 2 != 0:
                total_sum -= sum(nums[start_index:end_index])
    return total_sum