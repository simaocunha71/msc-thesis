
def max_Product(nums):
    return max(map(max, zip(*[sorted(nums)[:i+1] for i in range(len(nums))])))


