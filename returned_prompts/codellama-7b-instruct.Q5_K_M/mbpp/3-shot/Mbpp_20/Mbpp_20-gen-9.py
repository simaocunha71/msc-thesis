
def is_woodall(n):
  str_num = str(n)
  for i in range(len(str_num)):
    if not str_num[i] == str_num[0]:
      return False
  return True


