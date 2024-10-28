
def find_Rotations(str):
  i = 0
  while True:
    if str[:i] == str[-i:]:
      return i
    i += 1


