def check_smaller(tup1, tup2):
  return all(a <= b for a, b in zip(tup1, tup2)) == False