
def check_smaller(tup1, tup2):
  for i, j in zip(tup1, tup2):
    if i >= j:
      return False
  return True


