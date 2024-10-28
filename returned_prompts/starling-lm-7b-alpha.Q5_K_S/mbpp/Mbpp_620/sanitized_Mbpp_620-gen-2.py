def largest_subset(nums):
    """
    Time:  O(nlogn)
    Space: O(n)
    """
    # Sort the numbers in the list.
    nums.sort()
    # Initialize the result as 1, as there is at least one element in the list.
    result = 1
    # Initialize left as the first number in the list.
    left = nums[0]
    # Initialize right as the second number in the list.
    right = nums[1]
    # Iterate over the list.
    for i in xrange(len(nums)):
        # Check if the left number is not divisible by the current left number.
        if left % nums[i] != 0:
            # If not divisible, then reset the left number as the current number.
            left = nums[i]
        # Check if the right number is not divisible by the current right number.
        if right % nums[i] != 0:
            # If not divisible, then reset the right number as the current number.
            right = nums[i]
        # Check if the current number is divisible by both the left and the right number.
        if nums[i] % left == 0 and nums[i] % right == 0:
            # If divisible, then update the result.
            result = max(result, right - left + 1)
    # Return the result.
    return result