def freq_count(nums: list) -> dict:
  count = {}
  for num in nums:
    if num in count:
      count[num] += 1
    else:
      count[num] = 1
  return count