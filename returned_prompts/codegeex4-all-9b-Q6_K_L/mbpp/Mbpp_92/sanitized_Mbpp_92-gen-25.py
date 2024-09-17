def is_undulating(n: int) -> bool:
  str_num = str(n)
  if len(str_num) < 3:
    return False
  for i in range(2, len(str_num)):
    if str_num[i] == str_num[i-1] == str_num[i-2]:
      return False
  return True