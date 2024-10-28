def Diff(list1:list,list2:list) -> list:
  return [i for i in list1 if i not in list2]