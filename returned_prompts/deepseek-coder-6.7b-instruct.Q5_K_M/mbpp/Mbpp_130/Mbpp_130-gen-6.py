
def max_occurrences(lst):
  count_dict = {i: lst.count(i) for i in lst}
  return max(count_dict, key=count_dict.get)


