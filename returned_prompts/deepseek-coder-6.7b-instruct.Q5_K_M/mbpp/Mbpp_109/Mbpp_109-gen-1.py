
def odd_Equivalent(s: str, k: int) -> int:
  s = s * k
  cnt, odds = 0, 0
  for n in map(int, s):
    odds += n & 1
    if n & 1:
      cnt += odds
  return cnt


