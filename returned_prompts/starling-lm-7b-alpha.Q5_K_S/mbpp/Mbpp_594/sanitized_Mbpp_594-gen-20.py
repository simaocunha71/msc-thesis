def diff_even_odd(nums:list) -> int:
  odd = next(i for i in nums if i % 2 != 0)
  even = next(i for i in nums if i % 2 == 0)
  return odd - even