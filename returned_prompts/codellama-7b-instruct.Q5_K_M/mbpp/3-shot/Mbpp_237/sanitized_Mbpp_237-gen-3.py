def check_occurences(my_list):
  result = {}
  for tuple in my_list:
    if tuple not in result:
      result[tuple] = 1
    else:
      result[tuple] += 1
  return result