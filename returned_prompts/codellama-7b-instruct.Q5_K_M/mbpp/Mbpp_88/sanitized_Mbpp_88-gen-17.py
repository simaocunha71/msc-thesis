def freq_count(my_list):
  frequency = {}
  for item in my_list:
    frequency[item] = frequency.get(item,0) + 1
  return frequency