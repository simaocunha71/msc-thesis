def diff_even_odd(nums: list) -> int:
  first_even = next((x for x in nums if x % 2 == 0), None)
  first_odd = next((x for x in nums if x % 2 != 0), None)
  if first_even is None or first_odd is None:
    return 0
  return first_even - first_odd


