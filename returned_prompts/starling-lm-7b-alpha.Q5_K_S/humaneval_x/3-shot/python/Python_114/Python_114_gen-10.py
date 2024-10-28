    def minSubArraySum(nums):
        minSum = float("inf")
        curSum = 0
        for num in nums:
            curSum += num
            if curSum < minSum:
                minSum = curSum
            if curSum < 0:
                curSum = 0
        return minSum


