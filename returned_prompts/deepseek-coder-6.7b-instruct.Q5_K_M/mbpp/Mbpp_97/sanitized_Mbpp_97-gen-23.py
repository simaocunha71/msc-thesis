from collections import Counter
def frequency_lists(lst):
  flat_list = [item for sublist in lst for item in sublist]
  return dict(Counter(flat_list))