def validate(n):
    digits = [int(d) for d in str(n)]
    freq = {}
    for d in digits:
        freq[d] = freq.get(d, 0) + 1
        if d > freq[d]:
            return False
    return True