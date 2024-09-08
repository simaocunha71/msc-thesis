def check_occurences(lst):
  occurences = {}
  for tup in lst:
    if tup in occurences:
      occurences[tup] += 1
    else:
      occurences[tup] = 1
  return occurences