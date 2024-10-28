
def minSubArraySum(nums):
    curr_sum = min_sum = float('inf')
    for num in nums:
        curr_sum += num
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return min_sum


def minSubArraySum2(nums):
    min_sum = float('inf')
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum > 0:
            curr_sum = 0
    return min_sum


def minSubArraySum3(nums):
    return min(minSubArraySum(nums), minSubArraySum2(nums))



# print(minSubArraySum([2, 3, 4, 1, 2, 4]))
# print(minSubArraySum([-1, -2, -3]))
# print(minSubArraySum3([2, 3, 4, 1, 2, 4]))
# print(minSubArraySum3([-1, -2, -3]))




















































```