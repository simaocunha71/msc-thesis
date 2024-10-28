
def count_same_pair(list1: list,list2: list) -> int:
  return len([i for i,j in zip(list1,list2) if i==j])


