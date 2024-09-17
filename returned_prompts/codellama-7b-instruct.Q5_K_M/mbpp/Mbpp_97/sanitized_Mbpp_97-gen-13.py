def frequency_lists(lists: list) -> dict:
  flattened = [item for sublist in lists for item in sublist]
  frequency = {}
  for element in flattened:
    if element in frequency:
      frequency[element] += 1
    else:
      frequency[element] = 1
  return frequency