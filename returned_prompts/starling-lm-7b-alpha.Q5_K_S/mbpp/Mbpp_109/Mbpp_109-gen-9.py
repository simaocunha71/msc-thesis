
def odd_Equivalent(s: str, rotate: int) -> int:
  s = "".join([s, s])
  count = 0
  for i in range(len(s)):
    if int(s[i]) % 2 != 0:
      count += 1
  return count


