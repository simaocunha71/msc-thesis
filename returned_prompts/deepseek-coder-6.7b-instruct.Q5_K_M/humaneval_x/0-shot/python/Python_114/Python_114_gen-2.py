
    # Initialize the minimum subarray sum as the sum of the whole array.
    min_sum = sum(nums)
    # Initialize the current sum as 0.
    cur_sum = 0
    # Iterate over the array.
    for i in range(len(nums)):
        # For each element, update the current sum.
        cur_sum += nums[i]
        # If the current sum is less than the minimum sum, update the minimum sum.
        if cur_sum < min_sum:
            min_sum = cur_sum
        # If the current sum is greater than 0, reset it to 0.
        if cur_sum > 0:
            cur_sum = 0
    # Return the minimum sum.
    return min_sum

# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Expected: 1
print(minSubArraySum([-1, -2, -3]))  # Expected: -6
print(minSubArraySum([1, 2, 3, 4]))  # Expected: 1
print(minSubArraySum([-1, 2, 3, -4, 5]))  # Expected: -6

# Note: This solution works because it maintains a running total of the elements in the array.
# If the running total ever drops below the current minimum, it updates the minimum.
# If the running total ever goes to 0 or higher, it resets the running total to 0.
# This ensures that the minimum subarray sum is always tracked.

# The time complexity of this solution is O(n) as it goes through the array once.
# The space complexity is O(1) as it only uses a constant amount of space.
<jupyter_output>
1
-6
1
-6
<jupyter_text>
Question 2: (Leetcode: 39. Combination Sum)Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.The same number may be chosen from candidates an