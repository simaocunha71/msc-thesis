def max_val(lst):
    nums = []
    for i in lst:
        if type(i) == int or type(i) == float:
            nums.append(i)
    return max(nums)