def frequency_lists(test_list):
  freq_dict = {}
  for sublist in test_list:
    for elem in sublist:
      if elem in freq_dict:
        freq_dict[elem] += 1
      else:
        freq_dict[elem] = 1
  return freq_dict