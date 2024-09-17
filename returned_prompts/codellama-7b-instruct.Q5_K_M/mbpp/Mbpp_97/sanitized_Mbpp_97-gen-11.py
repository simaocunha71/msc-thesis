def frequency_lists(lists):
  flattened_list = [item for sublist in lists for item in sublist]
  frequency_dict = {}
  for i in flattened_list:
    if i in frequency_dict:
      frequency_dict[i] += 1
    else:
      frequency_dict[i] = 1
  return frequency_dict