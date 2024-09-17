def count_occurance(s):
  count = 0
  for i in range(len(s)-1):
    if s[i:i+2] == "std":
      count += 1
  return count