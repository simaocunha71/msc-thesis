
def count_Substrings(str):
  count = 0
  for i in range(len(str)):
    for j in range(i, len(str)):
      if sum(int(x) for x in str[i:j+1]) == len(str[i:j+1]):
        count += 1
  return count


