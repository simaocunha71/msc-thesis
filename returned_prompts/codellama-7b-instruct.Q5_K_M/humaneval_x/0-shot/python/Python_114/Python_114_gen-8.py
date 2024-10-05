
    def minSubArraySum(nums):
        if not nums:
            return 0
        return min(sum(nums[i:j]) for i in range(len(nums)) for j in range(i+1, len(nums)+1))

### 19. 

