
def find_Rotations(str1) -> int:
  if len(str1) == 0:
    return 0
  for i in range(len(str1)):
    if str1 == str1[i:]+str1[:i]:
      return len(str1) - i
  return len(str1)


