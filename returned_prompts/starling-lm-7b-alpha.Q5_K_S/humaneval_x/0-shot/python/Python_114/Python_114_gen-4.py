
# O(n) solution
def minSubArraySum(nums):
    min_sum = float("inf")
    cur_sum = 0
    for num in nums:
        cur_sum += num
        if cur_sum < min_sum:
            min_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return min_sum

# O(nlogn) solution
def minSubArraySum(nums):
    # Using heapq to find smallest sum of nums[i:j]
    from heapq import heapify, heappop, heappush
    min_sum = float("inf")
    cur_sum = 0
    heap = []
    for i in range(len(nums)):
        cur_sum += nums[i]
        heappush(heap, nums[i])
        while cur_sum < min_sum:
            min_sum = cur_sum
            if len(heap) > 0:
                cur_sum -= heappop(heap)
        while cur_sum > 0:
            cur_sum -= heappop(heap)
    return min_sum

# O(n^2) solution
def minSubArraySum(nums):
    min_sum = float("inf")
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            cur_sum = sum(nums[i:j+1])
            if cur_sum < min_sum:
                min_sum = cur_sum
    return min_sum

# Time:  O(n^2)
# Space: O(1)
class Solution(object):
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, nums, k):
        length = len(nums)
        result = float("inf")
        left = 0
        cur_sum = 0
        for right in xrange(length):
            cur_sum += nums[right]
            while cur_sum >= k:
                cur_sum -= nums[left]