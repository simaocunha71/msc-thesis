def len_log(words):
  lengths = []
  for w in words:
    lengths.append(len(w))
  return max(lengths)