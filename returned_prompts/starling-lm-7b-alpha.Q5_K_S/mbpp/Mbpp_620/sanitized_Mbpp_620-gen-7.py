def largest_subset(nums):
    """
    Given an array of numbers, return the size of the largest subset of numbers so that every pair is divisible.
    """
    # Create a dictionary to store the divisibility of each number
    divisibility = {}
    for num in nums:
        divisibility[num] = 1
        # If the number is already in the dictionary, update its divisibility
        if num in divisibility:
            for key in divisibility:
                if key % num == 0:
                    divisibility[num] = max(divisibility[num], divisibility[key] + 1)
    # Return the size of the largest subset
    return max(divisibility.values())