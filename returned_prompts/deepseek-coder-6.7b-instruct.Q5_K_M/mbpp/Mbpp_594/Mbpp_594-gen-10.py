
def diff_even_odd(lst):
    even_nums = [x for x in lst if x % 2 == 0]
    odd_nums = [x for x in lst if x % 2 != 0]
    return abs(even_nums[0] - odd_nums[0])


