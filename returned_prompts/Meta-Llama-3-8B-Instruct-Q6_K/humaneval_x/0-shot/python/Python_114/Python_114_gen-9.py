    # Initialize the minimum sum and the current sum to positive infinity
    min_sum = float('inf')
    current_sum = 0

    # Initialize the start of the window to 0
    start = 0

    # Iterate over the array
    for end in range(len(nums)):
        # Add the current element to the current sum
        current_sum += nums[end]

        # While the current sum is greater than or equal to 0
        while current_sum >= 0:
            # Update the minimum sum
            min_sum = min(min_sum, current_sum)

            # Subtract the element at the start of the window from the current sum
            current_sum -= nums[start]

            # Move the start of the window to the right
            start += 1

    # Return the minimum sum
    return min_sum

# Test the function
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6
print(minSubArraySum([1]))  # Output: 1
print(minSubArraySum([-1]))  # Output: -1
print(minSubArraySum([1, 2, 3, 4, 5]))  # Output: 1
print(minSubArraySum([1, -2, 3, 4, -5]))  # Output: -5
print(minSubArraySum([1, 2, 3, 4, 5, -6]))  # Output: -6
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12]))  # Output: -12
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))  # Output: -10
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))  # Output: 1
print(minSubArraySum([-