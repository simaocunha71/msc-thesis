def odd_length_sum(nums):
    return sum(sum(nums[i-j:i+j+1]) for i in range(len(nums)) for j in range(1, len(nums)) if i-j>=0 and i+j+1<=len(nums) and (i-j)%2!=0)