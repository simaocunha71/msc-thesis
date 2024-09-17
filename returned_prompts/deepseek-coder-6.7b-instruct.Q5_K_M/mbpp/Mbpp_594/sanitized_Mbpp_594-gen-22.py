def diff_even_odd(lst):
  even_nums = [i for i in lst if i % 2 == 0]
  odd_nums = [i for i in lst if i % 2 != 0]
  return abs(even_nums[0] - odd_nums[0])