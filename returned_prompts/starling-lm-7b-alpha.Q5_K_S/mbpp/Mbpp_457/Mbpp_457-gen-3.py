
def Find_Min(list_of_lists):
  min_len = len(list_of_lists[0])
  for i in range(len(list_of_lists)):
    if len(list_of_lists[i]) < min_len:
      min_len = len(list_of_lists[i])
  return min_len


