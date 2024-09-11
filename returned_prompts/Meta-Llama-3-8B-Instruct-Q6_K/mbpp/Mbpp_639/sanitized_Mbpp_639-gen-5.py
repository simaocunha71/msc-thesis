def sample_nam(lst):
  return sum(len(name) for name in lst if name[0].isupper())  # Check if the name starts with uppercase letter