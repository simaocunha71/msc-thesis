
def count_Substrings(s):
  n = len(s)
  res = 0
  for i in range(n):
    for j in range(i+1,n+1):
      if sum(map(int,s[i:j])) == j-i:
        res += 1
  return res


