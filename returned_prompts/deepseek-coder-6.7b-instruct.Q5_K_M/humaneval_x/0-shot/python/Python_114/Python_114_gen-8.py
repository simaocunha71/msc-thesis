
    if not nums:
        return 0

    current_sum = min_sum = nums[0]
    for num in nums[1:]:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
        
    return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # 1
print(minSubArraySum([-1, -2, -3]))  # -6
print(minSubArraySum([1, -1, -2, 1]))  # -3
print(minSubArraySum([-2, -3, 1]))  # -5
print(minSubArraySum([-2, -3, 5]))  # -8
print(minSubArraySum([2, 3, -4, 1, 2, 4]))  # -6
print(minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # -10

Explanation:

The function uses Kadane's algorithm to find the minimum sum of any non-empty sub-array.
The idea is to keep track of the current sum and the minimum sum found so far.
If the current number is smaller than the current sum plus the current number,
we update the current sum to be the current number, else we keep adding the current number to the current sum.
We then update the minimum sum if the current sum is smaller than the minimum sum.
Finally, we return the minimum sum.
'''

# Code:

def minSubArraySum(nums):
    if not nums:
        return 0

    current_sum = min_sum = nums[0]
    for num in nums[1:]:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
        
    return min_sum

# Test Cases:

print(minSubArraySum([2, 3, 4, 1, 2, 4]))