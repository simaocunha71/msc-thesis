
def count_samepair(list1:list,list2:list,list3:list) -> int:
  count = 0
  for i in range(len(list1)):
    if list1[i] == list2[i] and list2[i] == list3[i]:
      count += 1
  return count


