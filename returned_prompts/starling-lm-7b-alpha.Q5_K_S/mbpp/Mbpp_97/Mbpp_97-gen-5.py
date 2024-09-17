
def frequency_lists(list_of_lists: list) -> dict:
  frequency_dict = {}
  for sublist in list_of_lists:
    for item in sublist:
      if item in frequency_dict:
        frequency_dict[item] += 1
      else:
        frequency_dict[item] = 1
  return frequency_dict


