
def frequency_lists(lists: list) -> dict:
  freq_dict = {}
  for i in lists:
    for j in i:
      if j in freq_dict.keys():
        freq_dict[j] += 1
      else:
        freq_dict[j] = 1
  return freq_dict


