
def diff_even_odd(nums):
  diff = 0
  for num in nums:
    if num % 2 == 0:
      if diff == 0:
        diff = num
    else:
      diff = num - diff
      break
  return diff


