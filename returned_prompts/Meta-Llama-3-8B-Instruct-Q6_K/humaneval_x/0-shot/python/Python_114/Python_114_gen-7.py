    # Initialize the minimum sum as infinity
    min_sum = float('inf')
    # Initialize the current sum as 0
    current_sum = 0
    # Initialize the start index as 0
    start = 0
    # Iterate over the array
    for end in range(len(nums)):
        # Add the current element to the current sum
        current_sum += nums[end]
        # If the current sum is less than the minimum sum, update the minimum sum
        while current_sum < min_sum:
            min_sum = current_sum
            # Move the start index to the right
            start = end + 1
            # Reset the current sum
            current_sum = 0
    # Return the minimum sum
    return min_sum
# Test the function
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6
print(minSubArraySum([1, 2, 3, 4, 5]))  # Output: 1
print(minSubArraySum([-1, 0, 1, -2, 3]))  # Output: -2
print(minSubArraySum([1, 2, 3, 4, 5, 6]))  # Output: 1
print(minSubArraySum([-1, -2, -3, -4, -5]))  # Output: -9
print(minSubArraySum([1, -2, 3, -4, 5]))  # Output: -2
print(minSubArraySum([-1, -2, 3, 4, 5]))  # Output: -2
print(minSubArraySum([1, 2, 3, -4, 5]))  # Output: -4
print(minSubArraySum([-1, -2, -3, -4, -5]))  # Output: -9
print(minSubArraySum([1, 1, 1, 1, 1]))  # Output: 1
print(minSubArraySum([1, 1, 1, 1, -1]))  # Output: -1
print(minSubArraySum([-1, -1, -1, -1, -1]))  # Output