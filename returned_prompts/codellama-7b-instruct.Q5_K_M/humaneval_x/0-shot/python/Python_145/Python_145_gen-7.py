
def order_by_points(nums):
    def key_func(x):
        return sum(int(i) for i in str(abs(x)))
    return sorted(nums, key=key_func)