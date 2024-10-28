
def find_rotations(str1,str2):
  if str1 == str2:
    return 0
  else:
    for i in range(len(str1)):
      if str1 == str2[i:]:
        return len(str1) - i
      elif str1[i:] == str2:
        return i
    return -1


