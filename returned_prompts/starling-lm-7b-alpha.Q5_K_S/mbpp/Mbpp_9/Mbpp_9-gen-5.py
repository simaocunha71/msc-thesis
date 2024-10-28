
def find_Rotations(str_):
  if len(str_) == 0:
    return 0
  for i in range(1, len(str_)):
    if str_[i:] == str_[0:i]:
      return i
  return len(str_)


