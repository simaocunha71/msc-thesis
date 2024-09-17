
def find_Rotations(str1: str) -> int:
  if len(str1) == 1:
    return 0
  else:
    if str1 == str1[::-1]:
      return 1
    else:
      for i in range(len(str1)):
        if str1[i:] == str1[:len(str1)-i] and str1[i:] != str1[::-1]:
          return len(str1) - i
      return len(str1) + 1


