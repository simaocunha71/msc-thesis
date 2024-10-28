
def validate(n):
    digits = [int(d) for d in str(n)]
    return all(digit <= count for digit, count in ((d, digits.count(d)) for d in digits))


