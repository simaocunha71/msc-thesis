def find_Rotations(str1: str) -> int:
  if len(str1) == 0:
    return 0
  s1 = set(str1)
  for i in range(len(str1)):
    if str1[i] not in s1:
      return i+1
  return 0