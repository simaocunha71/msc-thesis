    def minSubArraySum(nums):
        cur, min_sum = 0, float('inf')
        for n in nums:
            cur += n
            if cur < min_sum:
                min_sum = cur
            if cur < 0:
                cur = 0
        return min_sum


