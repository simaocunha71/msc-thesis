
def diff_even_odd(nums: list) -> int:
  even = next((x for x in nums if x % 2 == 0), None)
  odd = next((x for x in nums if x % 2 == 1), None)
  return odd - even


