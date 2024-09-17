def frequency_lists(lists:list):
  freq_dict = {}
  for i in lists:
    for j in i:
      if j not in freq_dict:
        freq_dict[j] = 1
      else:
        freq_dict[j] += 1
  return freq_dict