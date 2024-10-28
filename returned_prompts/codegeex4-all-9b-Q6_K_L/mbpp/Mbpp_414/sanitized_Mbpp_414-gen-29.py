def overlapping(seq1: list, seq2: list) -> bool:
  if set(seq1) & set(seq2):
    return True
  else:
    return False