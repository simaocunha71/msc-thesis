def overlapping(seq1, seq2):
  if any(x in seq2 for x in seq1):
    return True
  else:
    return False