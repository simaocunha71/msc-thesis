def max_Product(nums):
    a = max(nums)
    b = max(nums, key = lambda x : -x)
    return (a,b)