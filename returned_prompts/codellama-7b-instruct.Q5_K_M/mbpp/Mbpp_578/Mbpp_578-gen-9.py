
def interleave_lists(list1,list2,list3):
  result = []
  for i,j,k in zip(list1,list2,list3):
    result.append(i)
    result.append(j)
    result.append(k)
  return result


