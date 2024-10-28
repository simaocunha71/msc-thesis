
def get_median(list1: list, list2: list, size: int) -> float:
  list3 = list1+list2
  list3.sort()
  if size % 2 == 0:
    return (list3[size//2-1]+list3[size//2])/2
  else:
    return list3[size//2]


