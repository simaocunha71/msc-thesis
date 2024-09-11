def filter_oddnumbers(lst):
  return [num for num in lst if num % 2 != 0]
  # return list(filter(lambda x: x % 2 != 0, lst)) # alternative solution