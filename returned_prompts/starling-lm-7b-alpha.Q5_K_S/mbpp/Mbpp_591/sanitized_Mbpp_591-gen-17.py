def swap_List(list1: list) -> list:
  first_ele = list1[0]
  last_ele = list1[-1]
  list1[-1] = first_ele
  list1[0] = last_ele
  return list1