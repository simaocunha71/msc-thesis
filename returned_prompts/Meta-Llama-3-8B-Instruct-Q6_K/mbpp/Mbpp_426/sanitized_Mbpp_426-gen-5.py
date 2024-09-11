def filter_oddnumbers(lst):
  return [i for i in lst if i%2 != 0]  # or return list(filter(lambda x: x%2 != 0, lst))