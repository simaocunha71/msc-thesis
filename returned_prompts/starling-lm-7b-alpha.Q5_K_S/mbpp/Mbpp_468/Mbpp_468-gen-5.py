
def max_product(nums):
    mult = 1
    max_mult = 0
    for i in nums:
        mult = max(mult * i, 1)
        max_mult = max(mult, max_mult)
    return max_mult


