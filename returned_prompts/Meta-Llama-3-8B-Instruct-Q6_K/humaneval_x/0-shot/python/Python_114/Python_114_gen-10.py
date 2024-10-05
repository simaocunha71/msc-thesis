    def minSubArraySum(nums):
        min_sum = float('inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)
            if current_sum > 0:
                current_sum = 0
        return min(min_sum, min(nums))
    # Test cases
    print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
    print(minSubArraySum([-1, -2, -3]))  # Output: -6
    print(minSubArraySum([1, 2, 3, 4, 5]))  # Output: 1
    print(minSubArraySum([1, -1]))  # Output: -1
    print(minSubArraySum([-1]))  # Output: -1
    print(minSubArraySum([1]))  # Output: 1
    print(minSubArraySum([0]))  # Output: 0
    print(minSubArraySum([]))  # Output: 0

