def count_Substrings(string):
  n = len(string)
  count = 0
  for i in range(n):
    for j in range(i+1, n+1):
      if sum(map(int, string[i:j])) == j - i:
        count += 1
  return count