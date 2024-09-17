
def remove_length(s, k):
  return ' '.join([w for w in s.split() if len(w) != k])


