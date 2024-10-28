def check_smaller(tup1: tuple,tup2: tuple) -> bool:
  for i in range(len(tup1)):
    if tup1[i] <= tup2[i]:
      return False
  return True