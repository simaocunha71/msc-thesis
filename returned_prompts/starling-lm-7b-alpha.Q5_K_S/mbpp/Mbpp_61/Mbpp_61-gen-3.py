
def count_Substrings(s: str) -> int:
  count = 0
  for i in range(len(s)):
    for j in range(i, len(s)):
      if sum(map(int, s[i:j + 1])) == j - i + 1:
        count += 1
  return count


