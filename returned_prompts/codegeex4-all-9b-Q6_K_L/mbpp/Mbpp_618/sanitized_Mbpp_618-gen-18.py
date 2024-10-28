def div_list(list1: list, list2: list) -> list:
  return [float(i)/float(j) for i,j in zip(list1, list2)]