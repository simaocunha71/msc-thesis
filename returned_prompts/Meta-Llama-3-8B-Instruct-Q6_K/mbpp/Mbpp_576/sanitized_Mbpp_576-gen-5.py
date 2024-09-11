def is_Sub_Array(lst1, lst2):
  return lst2 in [lst1[i:] for i in range(len(lst1))]