
def freq_count(nums:list) -> dict:
  freq = {}
  for num in nums:
    if num in freq:
      freq[num] += 1
    else:
      freq[num] = 1
  return freq


