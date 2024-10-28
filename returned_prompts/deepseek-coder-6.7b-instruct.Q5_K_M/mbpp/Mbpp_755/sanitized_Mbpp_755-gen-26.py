def second_smallest(nums: list) -> int:
  first, second = float('inf'), float('inf')
  for n in nums:
    if n <= first:
      first, second = n, first
    elif n < second:
      second = n
  return second