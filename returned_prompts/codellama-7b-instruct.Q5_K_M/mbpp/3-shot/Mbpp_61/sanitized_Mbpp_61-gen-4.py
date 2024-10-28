def count_Substrings(string: str) -> int:
  count = 0
  for i in range(len(string)):
    for j in range(i,len(string)):
      if sum(int(x) for x in string[i:j+1]) == len(string[i:j+1]):
        count+=1
  return count