
def interleave_lists(list1,list2,list3):
  return [list1[i%len(list1)] for i in range(len(list1)+len(list2)+len(list3))] + [list2[i%len(list2)] for i in range(len(list1)+len(list2)+len(list3))] + [list3[i%len(list3)] for i in range(len(list1)+len(list2)+len(list3))]


