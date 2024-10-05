    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum > 0:
            current_sum = 0
    return min_sum
# Test the function
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6
print(minSubArraySum([1, 2, 3, 4, 5]))  # Output: 1
print(minSubArraySum([-10, -5, 0, 5]))  # Output: -5
print(minSubArraySum([1, -1]))  # Output: -1
print(minSubArraySum([1, 1, 1, 1]))  # Output: 1
print(minSubArraySum([-2, -3, -1, -4]))  # Output: -4
print(minSubArraySum([-1, -2, -3, -4]))  # Output: -6
print(minSubArraySum([1, 2, 3, 4, 5, 6]))  # Output: 1
print(minSubArraySum([-10, -5, -2, -1]))  # Output: -10
print(minSubArraySum([-10, -5, -2, -1, 1]))  # Output: -10
print(minSubArraySum([1, 2, 3, 4, 5, 6, 7]))  # Output: 1
print(minSubArraySum([-10, -5, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: -10
print(minSubArraySum([-1, -2, -3, -4, -5]))  # Output: -5
print(minSubArraySum([-1, -2, -3, -4, -5, -6]))  # Output: -6
print(minSubArraySum([-1, -2, -3, -4, -5, -6, -7]))  # Output: -7