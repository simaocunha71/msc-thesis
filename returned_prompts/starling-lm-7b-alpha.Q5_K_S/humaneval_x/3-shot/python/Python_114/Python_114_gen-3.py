    def minSubArraySum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = float('inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum < result:
                result = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return result


