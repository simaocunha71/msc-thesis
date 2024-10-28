
def specialFilter(nums):
    return len(list(filter(lambda x: x > 10 and str(x)[0] % 2 != 0 and str(x)[-1] % 2 != 0, nums)))

