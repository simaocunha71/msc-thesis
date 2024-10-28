def frequency_lists(lists):
  frequency = {}
  for lst in lists:
    for item in lst:
      if item in frequency:
        frequency[item] += 1
      else:
        frequency[item] = 1
  return frequency