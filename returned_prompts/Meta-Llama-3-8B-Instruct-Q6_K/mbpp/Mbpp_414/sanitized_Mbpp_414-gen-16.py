def overlapping(sequence1, sequence2):
    for value in sequence1:
        if value in sequence2:
            return True
    return False