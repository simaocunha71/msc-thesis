def frequency_lists(lists):
  frequency = {}
  for sublist in lists:
    for item in sublist:
      if item in frequency:
        frequency[item] += 1
      else:
        frequency[item] = 1
  return frequency