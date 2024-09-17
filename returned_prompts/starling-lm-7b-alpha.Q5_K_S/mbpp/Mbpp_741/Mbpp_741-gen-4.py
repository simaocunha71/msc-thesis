
def all_Characters_Same(string):
  for i in range(len(string)-1):
    if string[i] != string[i+1]:
      return False
  return True


