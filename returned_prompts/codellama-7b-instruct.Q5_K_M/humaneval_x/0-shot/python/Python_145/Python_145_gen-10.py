
def order_by_points(nums):
    # sort based on sum of digits
    sorted_nums = sorted(nums, key=lambda x: sum(map(int, str(abs(x)))))
    # sort based on index in original list
    sorted_nums.sort(key=nums.index)
    return sorted_nums

