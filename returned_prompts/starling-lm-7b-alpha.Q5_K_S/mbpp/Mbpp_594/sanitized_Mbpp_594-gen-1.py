from typing import List
def diff_even_odd(nums: List[int]) -> int:
    odd_nums = [n for n in nums if n % 2 != 0]
    even_nums = [n for n in nums if n % 2 == 0]
    if len(odd_nums) > 0 and len(even_nums) > 0:
        return odd_nums[0] - even_nums[0]
    else:
        raise ValueError('List must contain at least one odd and one even number')