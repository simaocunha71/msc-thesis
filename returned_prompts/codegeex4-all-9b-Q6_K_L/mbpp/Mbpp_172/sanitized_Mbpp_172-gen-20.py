def count_occurance(s: str):
  count = 0
  for i in range(len(s)):
    if s[i:i+3] == 'std':
      count += 1
  return count