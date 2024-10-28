from collections import Counter
def frequency_lists(lst):
  flattened_list = [item for sublist in lst for item in sublist]
  return dict(Counter(flattened_counter))