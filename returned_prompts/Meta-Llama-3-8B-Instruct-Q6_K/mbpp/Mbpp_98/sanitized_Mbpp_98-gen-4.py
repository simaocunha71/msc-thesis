import math
def multiply_num(nums):
    product = 1
    for num in nums:
        product *= num
    return product / len(nums) if nums else 0
    #return math.prod(nums) / len(nums) if nums else 0 #python3.8 and above
    # return functools.reduce(lambda x,y: x*y,nums)/len(nums) if nums else 0 #python3.9 and above
    # return functools.reduce(lambda x,y: x*y,nums,1.0)/len(nums) if nums else 0 #python3.9 and above
    # return functools.reduce(lambda x,y: x*y,nums,1)/len(nums) if nums else 0 #python3.9 and above