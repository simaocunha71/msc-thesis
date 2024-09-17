def count_Substrings(s: str) -> int:
  count = 0
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      substr = s[i:j]
      if sum(int(digit) for digit in substr) == len(substr):
        count += 1
  return count

