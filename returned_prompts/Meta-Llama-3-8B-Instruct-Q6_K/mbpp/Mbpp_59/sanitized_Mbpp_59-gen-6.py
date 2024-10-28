def is_octagonal(n):
    if n < 1:
        return None
    return int((8*n**3 - 13*n**2 + 7*n) / 2)  # This is the nth octagonal number. The formula is derived from the sequence 1, 1, 2, 1, 3, 2, 4, 1, 6, 5, ... which is the sequence of octagonal numbers. The formula is derived from the recurrence relation defined in the sequence.