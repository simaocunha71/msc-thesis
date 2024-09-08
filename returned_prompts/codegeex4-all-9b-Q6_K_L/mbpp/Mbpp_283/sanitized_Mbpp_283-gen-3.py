def validate(n):
    freq = {}
    for digit in str(n):
        freq[digit] = freq.get(digit, 0) + 1
    for digit, count in freq.items():
        if count > int(digit):
            return False
    return True