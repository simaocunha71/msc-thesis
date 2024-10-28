
def check_smaller(tup1, tup2):
  if len(tup1) != len(tup2):
    return False
  for i in range(len(tup1)):
    if tup1[i] >= tup2[i]:
      return False
  return True


