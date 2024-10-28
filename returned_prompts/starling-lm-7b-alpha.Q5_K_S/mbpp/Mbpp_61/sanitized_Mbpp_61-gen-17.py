def count_Substrings(s:str) -> int:
  length = len(s)
  count = 0
  for i in range(length):
    for j in range(i+1, length+1):
      sub = s[i:j]
      if sum(map(int, sub)) == len(sub):
        count += 1
  return count