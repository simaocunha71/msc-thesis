def count_reverse_pairs(s):
  count = 0
  for i in range(len(s)):
    for j in range(i+1, len(s)):
      if s[i] == s[j][::-1]:
        count += 1
  return count