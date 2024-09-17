def odd_Equivalent(s: str, n: int) -> int:
  s = s * (n + 1)
  ans = 0
  for i in range(len(s)):
    if int(s[i]) % 2 == 1:
      ans += 1
  return ans