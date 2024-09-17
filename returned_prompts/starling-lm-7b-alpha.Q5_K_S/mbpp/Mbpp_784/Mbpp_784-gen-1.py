
def mul_even_odd(nums: list) -> int:
  even_nums = [x for x in nums if x % 2 == 0][0]
  odd_nums = [x for x in nums if x % 2 != 0][0]
  return even_nums * odd_nums


