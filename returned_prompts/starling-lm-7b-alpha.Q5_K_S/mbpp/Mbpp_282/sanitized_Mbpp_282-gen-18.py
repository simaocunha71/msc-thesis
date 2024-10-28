def sub_list(list1: list, list2: list) -> list:
  sub_list = []
  for i in range(len(list1)):
    sub_list.append(list1[i] - list2[i])
  return sub_list