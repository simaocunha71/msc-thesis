def find_Max_Num(lst):
  lst.sort(reverse=True)
  return int("".join(map(str, lst)))