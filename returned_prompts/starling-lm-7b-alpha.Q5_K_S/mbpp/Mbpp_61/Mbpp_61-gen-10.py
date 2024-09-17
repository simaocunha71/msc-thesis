
def count_Substrings(string):
  count = 0
  for i in range(len(string)):
    for j in range(i, len(string)):
      if sum(map(int, string[i:j+1])) == j - i + 1:
        count += 1
  return count


