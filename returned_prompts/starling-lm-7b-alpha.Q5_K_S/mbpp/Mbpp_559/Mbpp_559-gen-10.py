def max_sub_array_sum(nums, limit):
    """
    Find the sum of the largest contiguous sublist in the given list
    """
    # Initialize result
    result = 0
    # Initialize current sum
    current_sum = 0
    # Initialize start
    start = 0

    # Iterate through the list
    for i in range(0, len(nums)):
        current_sum += nums[i]
        # If current sum exceeds the limit, reset the start index and current sum
        if current_sum > limit:
            while current_sum > limit:
                current_sum -= nums[start]
                start += 1
        # If current sum is greater than result, update result
        if current_sum > result:
            result = current_sum
    return result


# assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
# assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 3) == 3
# assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, 6, -3], 5) == 8
# assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, 6, 7, 8, -3], 8) == 15
# assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, 6, 7, 8, 9, 0, -3], 9) == 24

def max_sub_array_sum(nums, limit):
    """
    Find the sum of the largest contiguous sublist in the given list
    """
    # Initialize result
    result = 0
    # Initialize current sum
    current_sum = 0
    # Initialize start
    start = 0

    # Iterate