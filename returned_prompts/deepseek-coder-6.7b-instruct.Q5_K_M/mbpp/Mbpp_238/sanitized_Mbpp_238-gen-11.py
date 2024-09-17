def number_of_substrings(string):
  return sum(i+1 for i in range(len(string)))