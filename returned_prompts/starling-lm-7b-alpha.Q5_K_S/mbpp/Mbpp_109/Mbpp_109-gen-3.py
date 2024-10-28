
def odd_Equivalent(s: str, n: int) -> int:
  while n > 0:
    if s[-1] == '1':
      s = s[:-1]
    else:
      s = s[:-1] + '1'
    n -= 1
  odd_nums = 0
  for i in s:
    if int(i) % 2 != 0:
      odd_nums += 1
  return odd_nums


