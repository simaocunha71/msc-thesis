def get_ludic(n: int) -> list:
  res = []
  for i in range(1, n+1):
    if is_lucid(i):
      res.append(i)
  return res
def is_lucid(n: int) -> bool:
  return str(n).count("4") == 1