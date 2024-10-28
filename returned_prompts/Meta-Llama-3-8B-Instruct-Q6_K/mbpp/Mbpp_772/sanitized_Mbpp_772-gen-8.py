def remove_length(s, k):
  words = s.split()
  new_s = ' '.join(word for word in words if len(word) != k)
  return new_s