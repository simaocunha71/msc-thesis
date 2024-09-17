
def get_median(list1, list2, size):
  list3 = list1 + list2
  list3.sort()
  median = len(list3)//2
  if median % 2 == 0:
    return (list3[median-1] + list3[median])/2.0
  else:
    return list3[median]


