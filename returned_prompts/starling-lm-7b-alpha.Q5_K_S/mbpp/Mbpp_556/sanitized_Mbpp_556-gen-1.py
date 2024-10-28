def find_Odd_Pair(nums,target):
    res=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]^nums[j])%2 == 1:
                res+=1
    return res