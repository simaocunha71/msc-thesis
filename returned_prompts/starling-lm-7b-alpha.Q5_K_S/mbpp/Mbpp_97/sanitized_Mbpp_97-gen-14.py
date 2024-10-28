def frequency_lists(nums_list: list) -> dict:
  freq = {}
  for i in nums_list:
    for j in i:
      if j in freq:
        freq[j] += 1
      else:
        freq[j] = 1
  return freq