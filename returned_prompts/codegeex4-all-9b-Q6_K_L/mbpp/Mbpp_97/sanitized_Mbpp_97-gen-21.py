def frequency_lists(nums: list) -> dict:
  freq_dict = {}
  for sublist in nums:
    for num in sublist:
      if num not in freq_dict:
        freq_dict[num] = 1
      else:
        freq_dict[num] += 1
  return freq_dict