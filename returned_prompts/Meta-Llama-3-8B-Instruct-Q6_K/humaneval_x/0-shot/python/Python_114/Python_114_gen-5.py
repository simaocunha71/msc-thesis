    min_sum = float('inf')
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > 0:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[left]
            left += 1

    return min_sum if min_sum != float('inf') else 0
# test the function
print(minSubArraySum([2, 3, 4, 1, 2, 4])) # Output: 1
print(minSubArraySum([-1, -2, -3])) # Output: -6
print(minSubArraySum([1])) # Output: 1
print(minSubArraySum([0])) # Output: 0
print(minSubArraySum([])) # Output: 0
print(minSubArraySum([-1])) # Output: -1
print(minSubArraySum([1, -2, 3])) # Output: -2
print(minSubArraySum([5, -3, 4, -1])) # Output: -1
print(minSubArraySum([1, 2, 3, 4, 5])) # Output: 1
print(minSubArraySum([1, 1, 1, 1, 1])) # Output: 1
print(minSubArraySum([-1, -2, -3, -4, -5])) # Output: -5
print(minSubArraySum([-1, 0, 1])) # Output: -1
print(minSubArraySum([1, 2, 3, 4, -5])) # Output: -5
print(minSubArraySum([-1, -2, 3, 4])) # Output: -2
print(minSubArraySum([1, 2, 3, 4])) # Output: 1
print(minSubArraySum([-1, 0, 1, 2])) # Output: -1
print(minSubArraySum([1, 2, 3, -4, 5])) # Output: -4
print(minSubArraySum([-1, -2, -3, 4])) # Output: -6
print(minSubArraySum([1, -2, 3, 4])) # Output: -2
print(minSubArraySum([-1, 0,