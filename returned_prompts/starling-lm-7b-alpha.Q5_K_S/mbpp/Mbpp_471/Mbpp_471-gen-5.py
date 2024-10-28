
def find_remainder(nums, mod):
    return reduce(lambda x, y: (x*y)%mod, nums)


