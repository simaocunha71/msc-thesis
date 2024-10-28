
def minSubArraySum(nums):
    min_sum = float('inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            min_sum = min(min_sum, curr_sum)
    return min_sum

# Time: O(n^2)
# Space: O(1)

# Optimization
def minSubArraySum(nums):
    min_sum = float('inf')
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        while curr_sum > 0:
            min_sum = min(min_sum, curr_sum)
            curr_sum -= nums[i]
            if i+1 < len(nums):
                curr_sum += nums[i+1]
    return min_sum if min_sum != float('inf') else 0

# Time: O(n)
# Space: O(1)

# Optimization
def minSubArraySum(nums):
    min_sum = float('inf')
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        min_sum = min(min_sum, curr_sum)
        if curr_sum > 0:
            curr_sum = 0
    return min_sum if min_sum != float('inf') else 0

# Time: O(n)
# Space: O(1)

# Optimization
def minSubArraySum(nums):
    min_sum = float('inf')
    curr_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum = min(curr_sum+nums[i], nums[i])
        min_sum = min(min_sum, curr_sum)
    return min_sum if min_sum != float('inf') else 0

# Time: O(n)
# Space: O(1)

# Optim