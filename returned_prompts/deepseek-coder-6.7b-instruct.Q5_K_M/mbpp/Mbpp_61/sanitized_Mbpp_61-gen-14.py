def count_Substrings(s):
  n = len(s)
  result = 0
  for i in range(1, n+1):
    for j in range(n-i+1):
      if j+i <= n:
        substring = s[j: j+i]
        if sum(int(ch) for ch in substring) == i:
          result += 1
  return result