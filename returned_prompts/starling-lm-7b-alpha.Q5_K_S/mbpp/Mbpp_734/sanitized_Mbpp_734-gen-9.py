def sum_Of_Subarray_Prod(nums):
    # Initialize result
    result = 0
    # Loop through all possible sublists
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # Calculate product of sublist elements and add to result
            result += reduce(lambda x, y: x * y, nums[i:j + 1])
    return result