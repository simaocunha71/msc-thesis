    def minSubArraySum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = float('inf')
        curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum < res:
                res = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return res


