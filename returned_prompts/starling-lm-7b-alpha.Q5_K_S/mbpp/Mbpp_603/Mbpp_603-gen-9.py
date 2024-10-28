
def get_ludic(n: int) -> list:
  lucid_numbers = []
  for i in range(1, n+1):
    if is_lucid(i):
      lucid_numbers.append(i)
  return lucid_numbers

def is_lucid(n: int) -> bool:
  s = str(n)
  s_length = len(s)
  for i in range(s_length):
    if s[i] != '1':
      if i != 0 and s[i] != '0':
        return False
  return True


