
def count_Substrings(s: str) -> int:
  count = 0
  for i in range(len(s)):
    for j in range(i,len(s)):
      if sum(int(x) for x in s[i:j+1]) == len(s[i:j+1]):
        count += 1
  return count


