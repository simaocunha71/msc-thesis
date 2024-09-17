def sum_list(list1: list,list2: list) -> list:
  return [sum(i) for i in zip(list1, list2)]