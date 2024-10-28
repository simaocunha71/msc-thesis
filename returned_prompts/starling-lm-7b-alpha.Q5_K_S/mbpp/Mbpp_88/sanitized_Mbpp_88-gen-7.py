def freq_count(nums):
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d