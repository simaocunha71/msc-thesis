def sum_Of_Subarray_Prod(nums):
    return sum([reduce(lambda x,y:x*y,nums[i:j+1]) for i in range(len(nums)) for j in range(i,len(nums))])