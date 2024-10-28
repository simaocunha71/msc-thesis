
def diff_even_odd(nums: list) -> int:
  even = filter(lambda x: x % 2 == 0, nums)
  odd = filter(lambda x: x % 2 != 0, nums)
  if len(even) == 0 or len(odd) == 0:
    return 0
  else:
    return even.pop() - odd.pop()


