def extract_index_list(l1: list,l2: list,l3: list) -> list:
  index_list = []
  for i in range(len(l1)):
    if l1[i] == l2[i] and l2[i] == l3[i]:
      index_list.append(l1[i])
  return index_list