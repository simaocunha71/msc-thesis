def overlapping(seq_1, seq_2):
  for elem in seq_1:
    if elem in seq_2:
      return True
  return False