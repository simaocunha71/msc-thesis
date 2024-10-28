def sequence(n):
    if n <= 1:
        return 1
    else:
        return sequence(sequence(n-1)) + sequence(n-sequence(n-1))