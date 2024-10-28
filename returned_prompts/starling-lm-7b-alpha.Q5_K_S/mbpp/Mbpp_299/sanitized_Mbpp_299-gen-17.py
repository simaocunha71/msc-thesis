def max_aggregate(list_of_tuples):
  max_list = []
  for i in list_of_tuples:
    if i[0] not in max_list:
      max_list.append(i[0])
      max_list.append(i[1])
  return max(max_list)