def armstrong_number(n):
  return sum(map(lambda x: int(x) ** len(str(n)), str(n))) == n