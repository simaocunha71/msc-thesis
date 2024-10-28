def max_difference(nums):
    # Convert the tuple list to a list of differences
    diff = [y - x for x, y in nums]
    # Return the maximum difference
    return max(diff)

