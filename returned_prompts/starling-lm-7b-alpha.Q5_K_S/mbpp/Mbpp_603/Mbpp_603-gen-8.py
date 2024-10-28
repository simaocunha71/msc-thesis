
def get_ludic(n: int) -> list:
  result = []
  for i in range(1,n+1):
    if is_lucid(i):
      result.append(i)
  return result

def is_lucid(n: int) -> bool:
  tmp = str(n)
  for i in range(1,len(tmp)):
    if (int(tmp[0])+int(tmp[i])) % 3 != int(tmp[i]):
      return False
  return True


