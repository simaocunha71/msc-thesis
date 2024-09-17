
def remove_length(text, k):
  return ' '.join([w for w in text.split() if len(w) != k])


