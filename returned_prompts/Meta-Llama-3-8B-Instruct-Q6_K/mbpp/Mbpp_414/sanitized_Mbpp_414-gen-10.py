def overlapping(seq1, seq2):
  for val in seq1:
    if val in seq2:
      return True
  return False