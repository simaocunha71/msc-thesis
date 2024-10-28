
from collections import Counter
def sort_counter(dict):
  sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
  return sorted_dict


