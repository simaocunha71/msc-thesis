def sum_negativenum(nums):
    # Initialize an empty list to store the negative numbers
    negative_nums = []
    # Traverse through the given list of numbers
    for num in nums:
        # If the number is negative, add it to the list
        if num < 0:
            negative_nums.append(num)
    # Return the sum of the negative numbers
    return sum(negative_nums)