def is_Sub_Array(sublist1:list, sublist2:list) -> bool:
  return set(sublist1).issubset(set(sublist2))

