def remove_length(s, k):
  return " ".join(i for i in s.split() if len(i) != k)