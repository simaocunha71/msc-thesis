def number_of_substrings(s):
  count = 0
  for i in range(0, len(s)):
    for j in range(i, len(s)):
      if s[i] != s[j]:
        count += 1
  return count