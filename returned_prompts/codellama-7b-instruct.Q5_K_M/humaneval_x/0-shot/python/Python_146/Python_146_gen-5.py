
def specialFilter(nums):
    return len(list(filter(lambda x: x > 10 and (str(x)[0] + str(x)[-1]) % 2 == 1, nums)))
