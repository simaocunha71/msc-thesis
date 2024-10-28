def frequency_lists(nums: list) -> dict:
  frequency = {}
  for num in nums:
    if num not in frequency:
      frequency[num] = 1
    else:
      frequency[num] += 1
  return frequency