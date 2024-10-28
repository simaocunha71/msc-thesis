
def find_Rotations(str1):
  length = len(str1)
  if length == 1:
    return 0
  for i in range(length):
    if str1 == str1[i:]:
      return length - i
  return length


