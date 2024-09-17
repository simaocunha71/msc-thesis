def left_insertion(list_num,new_num):
  if new_num<=list_num[0]:
    return 0
  if new_num>list_num[-1]:
    return len(list_num)
  for i in range(len(list_num)):
    if new_num<list_num[i]:
      return i