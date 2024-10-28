def max_difference(tuple_list):
  tuple_list = sorted(tuple_list, key = lambda x: x[0])
  max_difference = 0
  for i in range(len(tuple_list)-1):
    max_difference = max(max_difference, tuple_list[i+1][1] - tuple_list[i][1])
  return max_difference