def max_Product(nums):
    largest_nums = hq.nlargest(2, nums)
    return tuple(largest_nums)