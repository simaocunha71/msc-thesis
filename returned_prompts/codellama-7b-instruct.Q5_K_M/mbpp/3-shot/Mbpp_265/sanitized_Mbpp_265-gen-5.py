def list_split(my_list,n):
  lists = []
  for i in range(0,len(my_list),n):
    lists.append(my_list[i:i+n])
  return lists