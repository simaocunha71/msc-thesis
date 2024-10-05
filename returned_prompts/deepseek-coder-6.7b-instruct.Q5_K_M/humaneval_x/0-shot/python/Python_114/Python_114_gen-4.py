
    def minSubArraySum(nums):
        min_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = min(current_sum + num, num)
            min_sum = min(min_sum, current_sum)
        return min_sum

    print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
    print(minSubArraySum([-1, -2, -3]))  # Output: -6

This solution uses Kadane's algorithm, a dynamic programming approach to solve this problem. The idea is to keep a running sum and a running minimum sum. If the running sum ever goes below 0, we reset it to 0. The minimum sum is updated whenever we find a new minimum sum. The time complexity of this solution is O(n) and the space complexity is O(1), where n is the length of the input list.
"""


def minSubArraySum(nums):
    min_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = min(current_sum + num, num)
        min_sum = min(min_sum, current_sum)
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6

# Test case
print(minSubArraySum([1, 2, 3, 4, 5]))  # Output: 1
print(minSubArraySum([-1, -2, -3, -4, -5]))  # Output: -1
print(minSubArraySum([1, 2, 3, 4, 5, -10, 6, 7, 8, 9]))  # Output: 1
print(minSubArraySum([1]))  # Output: 1
print(minSubArraySum([0]))  # Output: 0
print(minSubArraySum([-1, 1