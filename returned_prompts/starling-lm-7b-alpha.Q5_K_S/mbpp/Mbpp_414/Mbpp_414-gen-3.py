
def overlapping(seq1: list, seq2: list) -> bool:
  return len(set(seq1) & set(seq2)) > 0


