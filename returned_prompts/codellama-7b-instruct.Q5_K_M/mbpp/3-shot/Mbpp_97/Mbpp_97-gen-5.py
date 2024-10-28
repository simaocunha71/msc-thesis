
def frequency_lists(list_of_lists: list) -> dict:
  flattened_list = [item for sublist in list_of_lists for item in sublist]
  frequency = {}
  for element in flattened_list:
    if element in frequency:
      frequency[element] += 1
    else:
      frequency[element] = 1
  return frequency


