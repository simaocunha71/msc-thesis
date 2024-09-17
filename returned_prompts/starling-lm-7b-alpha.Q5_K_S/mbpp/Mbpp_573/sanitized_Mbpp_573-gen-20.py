def unique_product(nums):
    return reduce(lambda x,y: x*y, set(nums))