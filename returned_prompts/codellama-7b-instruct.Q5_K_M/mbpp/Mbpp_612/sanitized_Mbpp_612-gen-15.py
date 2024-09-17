def merge(my_list):
  result = [[],[]]
  for sublist in my_list:
    result[0].append(sublist[0])
    result[1].append(sublist[1])
  return result