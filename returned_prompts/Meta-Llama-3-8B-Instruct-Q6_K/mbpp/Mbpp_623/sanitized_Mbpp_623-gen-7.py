def nth_nums(nums, n):
    return [x**n for x in nums]  # or return list(map(lambda x: x**n, nums)) for older python versions
    # or return [pow(x, n) for x in nums] for older python versions without lambda function