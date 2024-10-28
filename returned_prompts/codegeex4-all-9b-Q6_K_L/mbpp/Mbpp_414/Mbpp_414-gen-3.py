def overlapping(seq1: list, seq2: list) -> bool:
  return any(i in seq1 for i in seq2)