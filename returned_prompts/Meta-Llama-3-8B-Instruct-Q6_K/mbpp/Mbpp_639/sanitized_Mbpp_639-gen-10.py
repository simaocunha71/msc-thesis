def sample_nam(lst):
  return sum(len(name) for name in lst if name[0].isupper())  # calculate the sum of the length of the names that start with uppercase letters