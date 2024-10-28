    def minSubArraySum(nums):
        res = float("inf")
        cur_sum = 0
        for i in nums:
            cur_sum += i
            if cur_sum < res:
                res = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return res

    def minSubArraySum(nums):
        res = float("inf")
        cur_sum = 0
        for i in nums:
            cur_sum += i
            res = min(res, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return res

    # def minSubArraySum(nums):
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             curSum = sum(nums[i:j+1])
    #             res = min(res, curSum)
    #     return res

    # def minSubArraySum(nums):
    #     return min(minSubArraySum(nums[i:]))


