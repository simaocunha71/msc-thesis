def number_of_substrings(s: str) -> int:
  num = 0
  for i in range(len(s)):
    for j in range(i,len(s)):
      if s[i] != s[j]:
        num += 1
  return num