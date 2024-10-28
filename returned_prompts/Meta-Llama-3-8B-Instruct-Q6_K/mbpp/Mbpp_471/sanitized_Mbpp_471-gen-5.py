def find_remainder(nums, n):
    return pow(reduce(lambda x, y: x*y, nums), -1, n) % n
def reduce(f, iterable):
    it = iter(iterable)
    value = next(it)
    for element in it:
        value = f(value, element)
    return value