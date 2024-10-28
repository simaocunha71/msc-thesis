def count_Occurrence(myTuple,myList):
  count = 0
  for i in myTuple:
    if i in myList:
      count+=1
  return count