
def large_product(list1,list2,n):
  result = []
  for i in range(n):
    for j in range(n):
      if list1[i] * list2[j] not in result:
        result.append(list1[i] * list2[j])
  return sorted(result,reverse = True)[:n]


