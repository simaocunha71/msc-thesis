def sub_list(list1:list,list2:list)->list:
  return [i-j for i,j in zip(list1,list2)]