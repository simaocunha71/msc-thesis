    min_sum = float('inf')  # Initialize the minimum sum as infinity
    current_sum = 0  # Initialize the current sum as 0

    for num in nums:
        current_sum += num  # Add the current number to the current sum
        min_sum = min(min_sum, current_sum)  # Update the minimum sum if necessary
        if current_sum > 0:  # If the current sum is greater than 0
            current_sum = 0  # Reset the current sum to 0

    return min_sum  # Return the minimum sum
# test the function
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6

