
    def minSubArraySum(nums):
        currSum = 0
        minSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum < 0:
                currSum = 0
            if minSum == 0:
                minSum = currSum
            else:
                minSum = min(minSum, currSum)
        return minSum
