def count_Substrings(s: str) -> int:
  count = 0
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      substring = s[i:j]
      if sum(int(c) for c in substring) == len(substring):
        count += 1
  return count