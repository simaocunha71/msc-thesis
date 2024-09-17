def overlapping(seq1: list, seq2: list) -> bool:
    return any(item in seq2 for item in seq1) or any(item in seq1 for item in seq2)