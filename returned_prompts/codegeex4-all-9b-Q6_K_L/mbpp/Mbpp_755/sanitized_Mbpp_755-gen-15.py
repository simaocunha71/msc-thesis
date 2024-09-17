def second_smallest(nums: list) -> int:
  first = second = float('inf')
  for num in nums:
    if num <= first:
      first, second = num, first
    elif num < second:
      second = num
  return second