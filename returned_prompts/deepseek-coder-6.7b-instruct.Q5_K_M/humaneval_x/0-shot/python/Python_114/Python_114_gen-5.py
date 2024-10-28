
    def minSubArraySum(nums):
        cur_sum, min_sum = float('inf'), float('inf')
        for num in nums:
            cur_sum = min(cur_sum + num, num)
            min_sum = min(min_sum, cur_md)
            cur_sum = num
        return min_sum if min_sum != float('inf') else max(nums)

