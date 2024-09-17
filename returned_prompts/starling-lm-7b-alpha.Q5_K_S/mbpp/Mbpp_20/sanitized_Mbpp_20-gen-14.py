def is_woodall(num):
  woodall_num = 0
  for i in str(num):
    woodall_num += int(i)
  if woodall_num == num:
    return True
  else:
    return False