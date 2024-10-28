
def order_by_points(nums):
    # Sort based on the sum of digits
    nums.sort(key=lambda x: sum(int(d) for d in str(x)))
    # Sort based on the index in original list if the sum of digits is the same
    nums.sort(key=nums.index)
    return nums
