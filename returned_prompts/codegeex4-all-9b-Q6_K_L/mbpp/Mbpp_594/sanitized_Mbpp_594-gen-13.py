def diff_even_odd(nums: list) -> int:
  first_even = None
  first_odd = None
  for num in nums:
    if num % 2 == 0:
      if first_even is None:
        first_even = num
    else:
      if first_odd is None:
        first_odd = num
  if first_even is None or first_odd is None:
    return None
  return first_even - first_odd