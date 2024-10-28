
def count_same_pair(list1: list, list2: list) -> int:
  return sum(a == b for a, b in zip(list1,list2))


