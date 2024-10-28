def check_occurences(tuples_list):
  result = {}
  for t in tuples_list:
    if t in result:
      result[t] += 1
    else:
      result[t] = 1
  return result