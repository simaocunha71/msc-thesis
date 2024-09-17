
def len_log(lst):
  lengths = []
  for word in lst:
    lengths.append(len(word))
  return max(lengths)


