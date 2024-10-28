def pair_wise(nums):
    out = []
    for i in range(len(nums)-1):
        out.append((nums[i],nums[i+1]))
    return out