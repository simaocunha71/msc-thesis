def max_occurrences(nums: list) -> int:
  frequency = {}
  for num in nums:
    if num in frequency:
      frequency[num] += 1
    else:
      frequency[num] = 1
  max_freq = max(frequency.values())
  for num, freq in frequency.items():
    if freq == max_freq:
      return num

