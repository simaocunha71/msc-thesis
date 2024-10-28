
def minSubArraySum(nums):
    curr_sum = min_sum = nums[0]
    for i in nums[1:]:
        curr_sum = min(curr_sum + i, i)
        min_sum = min(min_sum, curr_sum)
    return min_sum

# Time: O(n)
# Space: O(1)

# Note: the above solution is not correct, and it should be modified as below.

def minSubArraySum(nums):
    min_sum = curr_sum = float('inf')
    for i in nums:
        curr_sum += i
        while curr_sum > 0:
            min_sum = min(min_sum, curr_sum)
            curr_sum -= nums[i - 1]
    return min_sum if min_sum != float('inf') else 0

# Time: O(n)
# Space: O(1)


# Another way to find the minimum sum of any non-empty sub-array is to use Kadane's algorithm.

def minSubArraySum(nums):
    max_sum = curr_sum = float('inf')
    for i in nums:
        curr_sum = max(curr_sum + i, i)
        max_sum = min(max_sum, curr_sum)
    return max_sum

# Time: O(n)
# Space: O(1)


# Another way to find the minimum sum of any non-empty sub-array is to use dynamic programming.

def minSubArraySum(nums):
    curr_sum = min_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum = min(curr_sum + nums[i], nums[i])
        min_sum = min(min_sum, curr_sum)
    return min_sum

# Time: O(n)
# Space: O(n)


```

In this example, we are given an array of integers and we need to find the minimum sum of any non-empty sub-array of the given array.

One