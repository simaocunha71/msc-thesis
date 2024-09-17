def remove_length(str, k):
  return ' '.join(i for i in str.split() if len(i) != k)