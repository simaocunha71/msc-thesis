def overlapping(seq1: list, seq2: list) -> bool:
    return any(item in seq2 for item in seq1)

