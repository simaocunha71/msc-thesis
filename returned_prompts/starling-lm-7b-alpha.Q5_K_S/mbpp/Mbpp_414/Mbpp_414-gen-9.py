
def overlapping(seq1: list,seq2: list) -> bool:
  for i in seq2:
    if i in seq1:
      return True
  return False


