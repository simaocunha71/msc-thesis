def frequency_lists(nums: list) -> dict:
  flat_nums = [num for sublist in nums for num in sublist]
  freq_dict = {}
  for num in flat_nums:
    freq_dict[num] = freq_dict.get(num, 0) + 1
  return freq_dict