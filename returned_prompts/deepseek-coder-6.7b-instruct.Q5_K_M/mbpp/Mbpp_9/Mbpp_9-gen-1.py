
def find_Rotations(str):
  n = len(str)
  temp = str + str
  for i in range(1, n):
    if (temp[i:] == str):
      return i
  return 1
"""
