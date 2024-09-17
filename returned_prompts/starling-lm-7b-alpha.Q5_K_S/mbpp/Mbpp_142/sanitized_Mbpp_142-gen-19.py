def count_samepair(list1, list2, list3):
  return sum(1 for a,b,c in zip(list1,list2,list3) if a==b==c)