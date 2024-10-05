
def double_the_difference(lst):
    if not lst:
        return 0
    odd_nums = [x for x in lst if x % 2 != 0 and x > 0]
    diff = max(odd_nums) - min(odd_nums)
    return diff * 2