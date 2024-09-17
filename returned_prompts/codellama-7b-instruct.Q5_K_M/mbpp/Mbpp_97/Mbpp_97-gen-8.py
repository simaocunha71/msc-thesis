
def frequency_lists(my_list):
  flattened_list = [item for sublist in my_list for item in sublist]
  freq_dict = {}
  for element in flattened_list:
    if element in freq_dict:
      freq_dict[element] += 1
    else:
      freq_dict[element] = 1
  return freq_dict


