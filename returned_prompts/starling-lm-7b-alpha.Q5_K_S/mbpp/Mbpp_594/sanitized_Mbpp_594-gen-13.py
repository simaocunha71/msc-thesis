def diff_even_odd(nums: list) -> int:
  even = [i for i in nums if i % 2 == 0]
  odd = [i for i in nums if i % 2 != 0]
  if len(even) == 0 or len(odd) == 0:
    return 0
  return even[0] - odd[0]