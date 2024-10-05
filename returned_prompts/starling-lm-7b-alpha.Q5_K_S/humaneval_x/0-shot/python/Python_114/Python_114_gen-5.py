
# The idea here is to use Kadane's algorithm to solve this problem
# The time complexity of this algorithm is O(n)

def minSubArraySum(nums):
    cur_sum = min_sum = nums[0]
    for i in range(len(nums)):
        cur_sum = min(cur_sum + nums[i], nums[i])
        min_sum = min(min_sum, cur_sum)
    return min_sum

# The above solution works well if all the numbers in the array are positive, but if there are negative numbers, we may need to modify the solution a little bit
# One of the possible modifications is to use the following code:

def minSubArraySum(nums):
    cur_sum, min_sum = 0, float('inf')
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum < min_sum:
            min_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return min_sum

# Another possible modification is to use the following code:

def minSubArraySum(nums):
    cur_sum = min_sum = float('inf')
    for i in range(len(nums)):
        cur_sum = min(cur_sum + nums[i], nums[i])
        if cur_sum < min_sum:
            min_sum = cur_sum
    return min_sum

# The above two solutions have the same time complexity of O(n), but the second solution has a smaller space complexity of O(1)

# The above two solutions can handle negative numbers well, but if the array contains 0, the first solution may lead to incorrect results
# For example, if the array is [0, 0, 0, 0, 0], the first solution will return 0, but the correct result should be 0
# To handle this situation, we can modify the solution as follows:

def minSubArraySum(nums):
    cur_sum = min_sum = float('inf')
    for i in range(len(nums)):
        cur_sum