def frequency_lists(nums: list) -> dict:
  freq_dict = {}
  for num in nums:
    for i in num:
      if i in freq_dict:
        freq_dict[i] += 1
      else:
        freq_dict[i] = 1
  return freq_dict