def pair_xor_Sum(nums: list,n: int):
    return sum(x^y for x,y in zip(nums,nums[n:]+nums[:n]))