def count_Pairs(nums,k):
    n = len(nums)
    c = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]!=nums[j]:
                c += 1
    return c