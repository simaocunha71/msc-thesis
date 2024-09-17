def all_Characters_Same(str):
  if len(str) == 0:
    return True
  for i in range(1, len(str)):
    if str[i] != str[0]:
      return False
  return True