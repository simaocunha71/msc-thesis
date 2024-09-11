def count_Substrings(s: str) -> int:
  count = 0
  for i in range(len(s)):
    temp_sum = 0
    for j in range(i, len(s)):
      temp_sum += int(s[j])
      if temp_sum == j - i + 1:
        count += 1
  return count