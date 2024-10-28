def number_of_substrings(s):
  return sum(s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1))